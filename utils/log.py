# coding=utf-8
import datetime
import os
import re

import logbook
from logbook import Logger, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler

from settings import LOG_DIR, PROJECT_NAME_EN, DEBUG, DAY_FORMAT, LOG_LEVEL


# 日志存放路径
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def log_type(record, handler=None):
    # pylint: disable=unused-argument
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=record.time,                              # 日志时间
        level=record.level_name,                       # 日志等级
        filename=os.path.split(record.filename)[-1],   # 文件名
        func_name=record.func_name,                    # 函数名
        lineno=record.lineno,                          # 行号
        msg=record.message                             # 日志内容
    )
    return log


def generate_logger():

    # 日志名称
    logger = Logger(PROJECT_NAME_EN, level=LOG_LEVEL)
    logbook.set_datetime_format("local")
    logger.handlers = []
    # 日志打印到文件
    log_file = TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % PROJECT_NAME_EN), date_format=DAY_FORMAT, bubble=True, encoding='utf-8')
    log_file.formatter = log_type
    logger.handlers.append(log_file)
    if DEBUG:
        # 日志打印到屏幕
        log_std = ColorizedStderrHandler(bubble=True)
        log_std.formatter = log_type
        logger.handlers.append(log_std)
    return logger


logger = generate_logger()


def get_log_last_date():
    if not os.path.exists(LOG_DIR):
        return None
    for file in os.listdir(LOG_DIR):
        # date_str = file[len(PROJECT_NAME_EN)+1:-4]
        # print(date_str)
        filepath = os.path.join(LOG_DIR, file)
        with open(filepath, "r", encoding='utf-8') as f:
            content = f.read()
            date_str_list = re.findall(r"--start_date=(.*?)--", content)
            if date_str_list:
                date = max([datetime.datetime.strptime(date, DAY_FORMAT) for date in list(set(date_str_list))])
                return date.strftime(DAY_FORMAT)
