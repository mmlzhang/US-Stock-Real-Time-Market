
"""

美股行情

"""
import time
import random
import datetime

import requests

from utils import json_loads, save_data, get_headers, get_quotation_date
from utils.dingtalk import send_dingding, Colors
from settings import DATE_FORMAT, DOWNLOAD_INTERVAL, sleep_hour
from utils.log import logger

s = requests.session()

# 行情字段
key_map = {
    "f12": "instrument",
    "f2": "最新价",
    "f3": "涨跌幅",
    "f4": "涨跌额",
    "f5": "成交量",
    "f7": "振幅(%)",
    "f8": "换手率(%)",
    "f9": "市盈率",
    "f10": "量比",
    'f14': 'name',
    "f15": "最高价",
    "f16": "最低价",
    "f17": "开盘价",
    "f18": "昨收",
    "f20": "市值",  # 美元
    "f21": "市值",  # 美元
    "f23": "市净率",
    "f115": "市盈率",
    "date": "date"
}

keys = ["f12", 'f14', "f2", "f3", "f4", "f5", "f7", "f8", "f9", "f10", "f15",
        "f16", "f17", "f18", "f20", "f21", "f23", "f115", "date"]
csv_header = [key_map.get(k) for k in keys]
filename = "stock_quotation"


def handler_quotation(data_list):
    quotations = []
    us_instruments = []
    for data in data_list:
        quotation = []
        for k in keys:
            if k == "date":
                quotation.append(get_quotation_date())
            if k == "f12":
                us_instruments.append(data.get(k))
            else:
                quotation.append(data.get(k))
        quotations.append(quotation)
    print(us_instruments)
    return quotations


def get_quotation():
    page_num = 1
    page_size = 10000
    fields = "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152"
    # k = ['f43', 'f44', 'f45', 'f46', 'f60', 'f71', 'f47', 'f48', 'f49', 'f161', 'f50', 'f55', 'f59', 'f84', 'f86',
    #  'f92', 'f116', 'f126', 'f152', 'f167', 'f164', 'f168', 'f169', 'f170', 'f171', 'f172']

    # fields = ",".join(keys)
    start_url = "http://{h}.push2.eastmoney.com/api/qt/clist/get?" \
                "cb=jQuery1124012264592664044649_1565663112714&pn={pn}&pz={pz}&po=1&np=1" \
                "&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:105,m:106,m:107" \
                "&fields={fields}" \
                "&_={t}"

    url = start_url.format(
        h=random.randint(1, 100), pn=page_num, pz=page_size,
        t=str(time.time()).replace(".", "")[:13], fields=fields)
    resp = s.get(url, headers = get_headers())
    data = json_loads(resp.text).get("data")
    quotations = handler_quotation(data.get("diff"))
    save_data(quotations, filename=filename)
    total = int(data.get("total"))
    logger.info("获取行情数据 {} 条".format(total))


def main():
    # time.sleep(60 * 60 * sleep_hour)
    send_dingding(title="获取美股行情数据", text=datetime.datetime.utcnow().strftime(DATE_FORMAT), color=Colors.INFO)
    save_data(csv_header, header=True, filename=filename)
    while True:
        get_quotation()
        time.sleep(DOWNLOAD_INTERVAL)
    #     if datetime.datetime.utcnow().hour >= 22:
    #         break
    # send_dingding(title="美股行情结束", text=datetime.datetime.utcnow().strftime(DATE_FORMAT), color=Colors.INFO)


if __name__ == '__main__':
    main()
