import os
from pathlib import Path
from urllib.parse import quote_plus
import uuid

DEFAULT_MQTT_HOST = "172.17.0.1"
DEFAULT_MQTT_PASSWORD = "v2x2022"  # user define
DEFAULT_REDIS_HOST = "172.17.0.1"
DEFAULT_REDIS_PASSWORD = "v2x2022"  # user define
DEFAULT_MYSQL_HOST = "172.17.0.1"
DEFAULT_MYSQL_USER = "dandelion"
DEFAULT_MYSQL_PASSWORD = "v2x2022"  # user define
DEFAULT_CLOUD_URL = "http://172.17.0.1:28300/api/v1"
DEFAULT_ALGORITHM_YAML_PATH = "/etc/cerebrum/algorithm.yaml"
DEFAULT_ALGORITHM_YAML = """
rsi_formatter:
  enable: true
  algo: "transform_driver.rsi_service"
pre_process_ai_algo:
  enable: true
  algos:
    complement:
      enable: true
      algo: "pre_process_ai_algo.algo_lib.complement"
    fusion:
      enable: true
      algo: "pre_process_ai_algo.algo_lib.fusion.algorithm"
    smooth:
      enable: true
      algo: "pre_process_ai_algo.algo_lib.smooth"
scenario_aglo:
  algos:
    collision_warning:
      enable: true
      name: "scenario_aglo.algo_lib.collision_warning"
    cooperative_lane_change:
      enable: true
      name: "scenario_aglo.algo_lib.cooperative_lane_change"
    do_not_pass_warning:
      enable: true
      name: "scenario_aglo.algo_lib.do_not_pass_warning"
    sensor_data_sharing:
      enable: true
      name: "scenario_aglo.algo_lib.sensor_data_sharing"
post_process_algo:
  algos:
    post_process:
      enable: true
      name: "post_process_algo.post_process"
"""
DELIMITER = "/"

db_server = os.getenv("db_server") or "mariadb"

sqlalchemy_w = {
    "url": "sqlite:///:memory:",
    "echo": True,
    "pool_recycle": 3600,
    "encoding": "utf-8",
}

if db_server == "mariadb":
    DB_HOST = os.getenv("mysql_host") or DEFAULT_MYSQL_HOST
    DB_PORT = 3306
    DB_USERNAME = os.getenv("mysql_user") or DEFAULT_MYSQL_USER
    DB_PASSWORD = os.getenv("mysql_password") or DEFAULT_MYSQL_PASSWORD
    sqlalchemy_w = {
        "url": f"mariadb+pymysql://{DB_USERNAME}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/dandelion?charset=utf8",
        "echo": True,
    }

redis = {
    "host": os.getenv("redis_host") or DEFAULT_REDIS_HOST,
    "port": 6379,
    "password": os.getenv("redis_password") or DEFAULT_REDIS_PASSWORD,
    "db": 1,
}

mqtt = {
    "host": os.getenv("mqtt_host") or DEFAULT_MQTT_HOST,
    "port": 1883,
    "client_id": uuid.uuid4().hex,
    "username": "root",
    "password": os.getenv("emqx_password") or DEFAULT_MQTT_PASSWORD,
}

cloud_server = os.getenv("cloud_url") or DEFAULT_CLOUD_URL
algorithm_yaml = os.getenv("algorithm_yaml") or DEFAULT_ALGORITHM_YAML_PATH


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    example = os.path.join(BASE_DIR, "etc", "algorithm.yaml.example")
    with open(example, "w") as f:
        f.write(DEFAULT_ALGORITHM_YAML.strip() + "\n")
