"""Plot benchmark curves of fusion algorithm."""
import copy
import matplotlib.pyplot as plt
from pre_process_ai_algo.algo_lib.fusion import Fusion
import time
from typing import Dict

# FPS = 10 interval = 100 ms
origin_radar_data = {
    "ab00000de": [
        {
            "guid": "ab00000de",
            "source": 3,
            "ptcId": 1,
            "width": 1.8,
            "length": 3.8,
            "secMark": 59060,
            "ptcType": "motor",
            "x": 90.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "source": 3,
            "ptcId": 1,
            "secMark": 59110,
            "ptcType": "motor",
            "x": 91,
            "y": 100,
            "width": 1.8,
            "length": 3.8,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "source": 3,
            "ptcId": 1,
            "secMark": 59160,
            "ptcType": "motor",
            "width": 1.8,
            "length": 3.8,
            "x": 91.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "source": 3,
            "ptcId": 1,
            "secMark": 59210,
            "ptcType": "motor",
            "width": 1.8,
            "length": 3.8,
            "x": 92,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "source": 3,
            "ptcId": 1,
            "secMark": 59260,
            "width": 1.8,
            "length": 3.8,
            "ptcType": "motor",
            "x": 92.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59310,
            "ptcType": "motor",
            "x": 93,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59360,
            "ptcType": "motor",
            "x": 93.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59410,
            "ptcType": "motor",
            "x": 94,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59460,
            "ptcType": "motor",
            "x": 94.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59510,
            "ptcType": "motor",
            "x": 95,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59560,
            "ptcType": "motor",
            "x": 95.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59610,
            "source": 3,
            "ptcId": 1,
            "ptcType": "motor",
            "x": 96,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59660,
            "source": 3,
            "ptcId": 1,
            "ptcType": "motor",
            "x": 96.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59710,
            "ptcType": "motor",
            "x": 97,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59760,
            "source": 3,
            "ptcId": 1,
            "ptcType": "motor",
            "x": 97.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59810,
            "ptcId": 1,
            "source": 3,
            "ptcType": "motor",
            "x": 98,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "source": 3,
            "ptcId": 1,
            "secMark": 59860,
            "ptcType": "motor",
            "x": 98.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59910,
            "ptcId": 1,
            "source": 3,
            "ptcType": "motor",
            "x": 99,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59960,
            "ptcId": 1,
            "source": 3,
            "ptcType": "motor",
            "x": 99.5,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
        {
            "guid": "ab00000de",
            "width": 1.8,
            "length": 3.8,
            "ptcType": "motor",
            "ptcId": 1,
            "source": 3,
            "secMark": 10,
            "x": 100,
            "y": 100,
            "speed": 500,
            "heading": 7200,
        },
    ],
    "ab00001de": [
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59060,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 90,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59110,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 90.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59160,
            "source": 4,
            "ptcId": 12,
            "ptcType": "motor",
            "x": 91,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59210,
            "source": 4,
            "ptcType": "motor",
            "x": 91.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59260,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 92,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59310,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 92.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59360,
            "source": 4,
            "ptcType": "motor",
            "x": 93,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59410,
            "source": 4,
            "ptcType": "motor",
            "x": 93.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59460,
            "source": 4,
            "ptcType": "motor",
            "x": 94,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59510,
            "source": 4,
            "ptcType": "motor",
            "x": 94.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "ptcId": 12,
            "width": 1.8,
            "length": 3.8,
            "secMark": 59560,
            "source": 4,
            "ptcType": "motor",
            "x": 95,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59610,
            "source": 4,
            "ptcType": "motor",
            "x": 95.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59660,
            "source": 4,
            "ptcType": "motor",
            "x": 96,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59710,
            "source": 4,
            "ptcType": "motor",
            "x": 96.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59760,
            "source": 4,
            "ptcType": "motor",
            "x": 97,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "ptcId": 12,
            "secMark": 59810,
            "source": 4,
            "ptcType": "motor",
            "x": 97.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "source": 4,
            "ptcId": 12,
            "secMark": 59860,
            "ptcType": "motor",
            "x": 98,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59910,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 98.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 59960,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 99,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
        {
            "guid": "ab00001de",
            "width": 1.8,
            "length": 3.8,
            "secMark": 10,
            "ptcId": 12,
            "source": 4,
            "ptcType": "motor",
            "x": 99.5,
            "y": 100,
            "speed": 1000,
            "heading": 7200,
        },
    ],
}


def expand_data(origin_data):
    """Expand data based on original data."""
    new_guid_number = len(origin_data)
    copied_guid_number = new_guid_number - 2
    new_guid = "ab" + str(new_guid_number).zfill(5) + "de"
    copied_guid = "ab" + str(copied_guid_number).zfill(5) + "de"
    new_obj_info = [i for i in origin_data[copied_guid]]
    origin_data[new_guid] = new_obj_info
    for i in new_obj_info:
        i["x"] += 100
        i["y"] += 100
    return origin_data


def calc_fusion_eff_fps(frames):
    """Count times algorithm can run in specific interval."""
    begin_time = time.time()
    count_process_times = 0
    sexp = Fusion()
    while time.time() - begin_time <= process_interval:
        _ = sexp.test_run(frames, matchPairs)
        count_process_times += 1
    return count_process_times


def calc_fusion_eff_time(frames):
    """Record the time spent processing a frame of data."""
    begin_time = time.time()
    sexp = Fusion()
    _ = sexp.test_run(frames, matchPairs)
    process_time = time.time() - begin_time
    return process_time * 1000


def draw_fusion_fps(x, y):
    """Draw the curve of fps result."""
    plt.plot(x, y)
    plt.xlabel("data amount (traffic participants/frame)", fontsize=13)
    plt.ylabel("algorithmic efficiency (times/second)", fontsize=13)
    plt.title("Fusion Algorithm Benchmark", fontsize=15)


def draw_fusion_time(x, y):
    """Draw the curve of time result."""
    plt.plot(x, y)
    plt.xlabel("data amount (traffic participants/frame)", fontsize=13)
    plt.ylabel("algorithmic efficiency (milliseconds/frame)", fontsize=13)
    plt.title("Fusion Algorithm Benchmark", fontsize=15)


max_id_amount = 100
benchmark_point_interval = 10
process_interval = 1  # s

"""fps"""

# matchPairs = {
#       "1.0": ["0.0", "125.0"],
#       "2.0": ["1.0", "124.0"]}
matchPairs: Dict[str, list] = {}  # 若没有前期历史数据就为空。


def draw_benchmark_fps(origin_data):
    """Drawing fps curve."""
    benchmark_point_x = []
    benchmark_point_y = []
    while len(origin_data) < max_id_amount:
        expand_data(origin_data)
        if len(origin_data) % benchmark_point_interval == 0:
            benchmark_point_x.append(len(origin_data))
            benchmark_point_y.append(calc_fusion_eff_fps(origin_data))
        print(len(origin_data))
    plt.figure(figsize=(8, 5))
    draw_fusion_fps(benchmark_point_x, benchmark_point_y)
    plt.show()


origin_radar_data1 = copy.deepcopy(origin_radar_data)
draw_benchmark_fps(origin_radar_data1)
plt.savefig(
    "fusion_algo_benchmark_fps_" + str(max_id_amount) + ".png", dpi=300
)
plt.savefig("fusion_algo_benchmark_fps_" + str(max_id_amount) + ".svg")

"""time"""

# matchPairs = {
#       "1.0": ["0.0", "125.0"],
#       "2.0": ["1.0", "124.0"]}
# matchPairs: Dict[str, list] = {}  # 若没有前期历史数据就为空。


def draw_benchmark_time(origin_data):
    """Drawing time curve."""
    benchmark_point_x = []
    benchmark_point_y = []
    while len(origin_data) < max_id_amount:
        expand_data(origin_data)
        if len(origin_data) % benchmark_point_interval == 0:
            benchmark_point_x.append(len(origin_data))
            benchmark_point_y.append(calc_fusion_eff_time(origin_data))
        print(len(origin_data))
    plt.figure(figsize=(8, 5))
    draw_fusion_time(benchmark_point_x, benchmark_point_y)
    plt.show()


origin_radar_data2 = copy.deepcopy(origin_radar_data)
draw_benchmark_time(origin_radar_data2)
plt.savefig(
    "fusion_algo_benchmark_time_" + str(max_id_amount) + ".png", dpi=300
)
plt.savefig("fusion_algo_benchmark_time_" + str(max_id_amount) + ".svg")
