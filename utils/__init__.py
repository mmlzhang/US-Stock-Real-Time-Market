

import os
import csv
import re
import json
import datetime

from settings import DATE_FORMAT, DATA_PATH, DAY_FORMAT, CSV_DELIMITER


def json_loads(text):
    resp_str = "{" + re.findall("\({(.*?)}\)", text)[0] + "}"
    return json.loads(resp_str)


def trans_date(timestamp):
    if not timestamp:
        return ""
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime(DATE_FORMAT)


def save_data(data, filename, header=False):
    dir_name = datetime.datetime.utcnow().strftime("%Y%m%d")
    dir_path = os.path.join(DATA_PATH, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = os.path.join(dir_path, filename)
    with open("{}.csv".format(file), "a", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=CSV_DELIMITER)
        if not header:
            writer.writerows(data)
        else:
            writer.writerow(data)


def save_df(df, symbol):
    dir_name = datetime.datetime.utcnow().strftime("%Y%m%d")
    dir_path = os.path.join(DATA_PATH, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    file = os.path.join(dir_path, symbol)
    df.to_csv("{}.csv".format(file), sep=CSV_DELIMITER)


def get_headers():
    return {
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'HAList=l-sh-124831-PR%u5D07%u5EFA%u8BBE; st_si=57245802690406; st_asi=delete; qgqp_b_id=f827da1c3659dffb5f8ea20417a474e7; ASP.NET_SessionId=sq3pczwwnfqutb1vci1shzvp; st_pvi=88926606265536; st_sp=2019-08-08%2010%3A17%3A12; st_inirUrl=http%3A%2F%2Fguba.eastmoney.com%2F; st_sn=57; st_psi=20190814091149561-113200301323-3005268963',
        'Cache-Control': 'max-age=0',
        'Proxy-Connection': 'keep-alive',
        'Host': 'quote.eastmoney.com'
    }


def get_quotation_date():
    """股票行情信息中的date字段记录的时间"""
    return datetime.datetime.now().strftime(DATE_FORMAT)
