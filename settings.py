
import os

from logbook import base


PROJECT_NAME = "美股行情"
PROJECT_NAME_EN = "US-Quotation"


DEBUG = True

sleep_hour = 5   # 测试用,后面加入到airflow中定时调度


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DAY_FORMAT = "%Y-%m-%d"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# 请求间隔 秒
DOWNLOAD_INTERVAL = 3

# 布隆过滤器哈希文件位置
BLOOM_FILE_PATH = os.path.join(BASE_DIR, ".bloom_filter")

# 日志文件位置
LOG_DIR = os.path.join(BASE_DIR, "log")
LOG_LEVEL = base.DEBUG

# 数据存储目录
DATA_PATH = os.path.join(BASE_DIR, "data")
if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

# IP 代理
proxies = {
    # 'http': 'http:192.168.145.38:43128',
    # 'https': 'http://192.168.145.38:43128'
}

DING_TALK_URL = "https://oapi.dingtalk.com/robot/send?" \
                "access_token={your_token}"

# csv 文件分隔符
# CSV_DELIMITER = "\t"
CSV_DELIMITER = ","
