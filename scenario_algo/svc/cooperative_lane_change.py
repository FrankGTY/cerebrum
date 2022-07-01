"""Call the cooperative lane change algorithm function."""

import orjson as json
from post_process_algo import post_process
from scenario_algo.algo_lib import cooperative_lane_change
from scenario_algo.svc.collision_warning import CollisionWarning
from transform_driver import consts


class CooperativeLaneChange:
    """Call the cooperative lane change algorithm function."""

    def __init__(self, kv, mqtt) -> None:
        """Class initialization."""
        self._kv = kv
        self._mqtt = mqtt
        self._exe = cooperative_lane_change.CooperativeLaneChange()

    async def run(self, params: dict, rsu_id: str, convert_info: list) -> None:
        """External call function."""
        his_info = await self._kv.get(
            CollisionWarning.HIS_INFO_KEY.format(rsu_id)
        )
        context_frames = (
            his_info["context_frames"]
            if his_info.get("context_frames")
            else {}
        )
        current_frame = (
            his_info["latest_frame"] if his_info.get("latest_frame") else {}
        )

        msg_rsc, info_for_show = self._exe.run(
            convert_info, context_frames, current_frame, params
        )
        self._mqtt.publish(
            consts.CLC_TOPIC.format(rsu_id),
            json.dumps(msg_rsc),
            0,
        )
        if msg_rsc["coordinates"]["driveSuggestion"]["suggestion"] > 0:
            for i in info_for_show["traj_list_for_show"]:
                post_process.convert_for_visual(i, rsu_id)
            post_process.convert_for_visual(info_for_show["ego_point"], rsu_id)
            # rsu，前端
            self._mqtt.publish(
                consts.SCENARIO_VISUAL_TOPIC.format(rsu_id),
                json.dumps([info_for_show]),
                0,
            )
