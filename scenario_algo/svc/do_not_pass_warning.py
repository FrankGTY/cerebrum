"""Call the do not pass algorithm function."""

import orjson as json
from post_process_algo import post_process
from scenario_algo.algo_lib import do_not_pass_warning
from scenario_algo.svc.collision_warning import CollisionWarning
from transform_driver import consts


class DoNotPass:
    """Call the do not pass algorithm function."""

    def __init__(self, kv, mqtt) -> None:
        """Class initialization."""
        self._kv = kv
        self._mqtt = mqtt
        self._exe = do_not_pass_warning.DoNotPass()

    async def run(self, params: dict, rsu_id: str, _: list) -> None:
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
            rsu_id, context_frames, current_frame, params
        )
        if info_for_show:
            post_process.convert_for_visual(info_for_show["ego_point"], rsu_id)
        if msg_rsc:
            # rsu 前端
            self._mqtt.publish(
                consts.DNP_TOPIC.format(rsu_id),
                json.dumps(msg_rsc),
                0,
            )
            self._mqtt.publish(
                consts.SCENARIO_VISUAL_TOPIC.format(rsu_id),
                json.dumps([info_for_show]),
                0,
            )
