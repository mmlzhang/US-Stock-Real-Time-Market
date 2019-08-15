
"""

美股指数

"""
import datetime
import time
import traceback

import requests

from settings import DATE_FORMAT, DOWNLOAD_INTERVAL, sleep_hour
from utils import json_loads, trans_date, save_data, get_headers, get_quotation_date
from utils.dingtalk import send_dingding, Colors
from utils.log import logger


s = requests.session()

key_map = {
    'f17': '今开',
    'f16': '最低价',
    'f5': '成交量',
    'f2': '最新价',
    'f15': '最高价',
    'f7': '振幅',
    'f4': '涨跌额',
    'f12': 'instrument',
    'f18': '昨收',
    'f14': 'name',
    'f124': 'us_date',
    'date': 'date'
}


keys = ["f12", "f14", "f2", "f4", "f5", "f7", "f15", "f16", "f17", "f18", 'f124', "date"]
csv_header = [key_map.get(k) for k in keys]
filename= "stock_index"


def handler_index(data_list):
    index_data_list = []
    for data in data_list:
        index_data = []
        for k in keys:
            if k == "f124":
                index_data.append(trans_date(data.get(k)))
            elif k == "date":
                index_data.append(get_quotation_date())
            else:
                index_data.append(data.get(k))
        index_data_list.append(index_data)
    return index_data_list


def get_index_data():

    url = "http://58.push2.eastmoney.com/api/qt/clist/get?" \
          "cb=jQuery1124005752417505401741_1565678085560&pn=1&pz=20&po=1&np=1" \
          "&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3" \
          "&fs=i:100.NDX,i:100.DJIA,i:100.SPX" \
          "&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107" \
          "&_=1565678085561"

    resp = s.get(url, headers=get_headers())

    data = json_loads(resp.text).get("data")
    index_data = handler_index(data.get("diff"))
    save_data(index_data, filename=filename)
    total = data.get("total")
    logger.info("获取数据 {} 条".format(total))


def main():
    # time.sleep(60 * 60 * sleep_hour)
    send_dingding(title="获取美股指数数据", text=datetime.datetime.utcnow().strftime(DATE_FORMAT), color=Colors.INFO)
    save_data(csv_header, header=True, filename=filename)
    while True:
        try:
            get_index_data()
        except Exception:
            err = traceback.format_exc()
            send_dingding(title="获取美股指数错误", text=str(err))
            logger.error(str(err))
        time.sleep(DOWNLOAD_INTERVAL)
    #     if datetime.datetime.utcnow().hour >= 22:
    #         break
    # send_dingding(title="美股指数结束", text=datetime.datetime.utcnow().strftime(DATE_FORMAT), color=Colors.INFO)


if __name__ == '__main__':
    main()
