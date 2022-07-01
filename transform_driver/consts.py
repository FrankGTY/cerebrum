"""Algorithm service consts and mqtt topic config."""
from config import devel as cfg

MaxSecMark = 60000  # 新四跨中对secMark的规定中的最大值
CoordinateUnit = 10**7  # 新四跨协议规定的经纬度单位转换unit


def topic_replace(topic: str, delimiter: str) -> str:
    """Topic delimiter conversion for mqtt."""
    return topic.replace("/", delimiter)


# RSM
RSM_DOWN_TOPIC = topic_replace("V2X/RSU/RSM/{}/DOWN", cfg.DELIMITER)
RSM_STD_ACK_TOPIC = topic_replace("V2X/RSU/RSM/{}/ACK", cfg.DELIMITER)
RSM_DAWNLINE_ACK_TOPIC = topic_replace(
    "V2X/RSU/RSM/{}/DAWNLINE/ACK", cfg.DELIMITER
)

# RSM visual
RSM_VISUAL_TOPIC = topic_replace(
    "V2X/DEVICE/{}/PARTICIPANT", cfg.DELIMITER
)

# RSI
RSI_DOWN_TOPIC = topic_replace("V2X/RSU/RSI/{}/DOWN", cfg.DELIMITER)
RSI_UP_TOPIC = topic_replace("V2X/DEVICE/{}/RSI/UP", cfg.DELIMITER)

# scenario
CW_TOPIC = topic_replace("V2X/RSU/CWM/{}/DOWN", cfg.DELIMITER)
SDS_TOPIC = topic_replace("V2X/RSU/SDS/{}/DOWN", cfg.DELIMITER)
CLC_TOPIC = topic_replace("V2X/RSU/CLC/{}/DOWN", cfg.DELIMITER)
DNP_TOPIC = topic_replace("V2X/RSU/DNP/{}/DOWN", cfg.DELIMITER)

# scenario visual
SCENARIO_VISUAL_TOPIC = topic_replace(
    "V2X/DEVICE/{}/APPLICATION", cfg.DELIMITER
)
