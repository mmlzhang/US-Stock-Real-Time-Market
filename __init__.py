
"""
f7 69.44  振幅 %
f26 20170419
f1 2
f25 -67.42
f22 4.88
f140 -
f62 -
f128 -
f152 2
f141 -
f115 -18.96  市盈率
f6 45596480.0
f8 21.75  换手率 %
f10 9.89  量比
f24 55.42
f5 39048520   成交量
f33 0.0
f23 1.34  市净率
f136 -
f13 105
f11 3.2
"""

"""
详情字段
f43: 最新价  /100 美元
f44: 最高价 /100 美元
f45: 最低价  /100 美元
f46: 今开 /100 美元
f60:  昨收 /100 美元
f71:  均价  /100 美元
f47:  成交量
f48:  成交额
f49:  外盘 美元
f161:  内盘 美元

f50: 量比  /100 
f55:  每股收益
f59: 2
f84: 总股本
f86: 1565654400
f92: 每股净资产
f116:  总市值 美元
f126: 0
f152: 2

f167:  市净率  / 100
f164:  市盈率 / 100  PE(ttm)

f168:  换手率 % /100
f169:  涨跌  % /100
f170:  涨幅  % /100
f171:  振幅  % /100
f172: ""    股息率
"""

# 详情页字段
info_map = {
    'f60': '昨收 /100 美元',
    'f71': '均价  /100 美元',
    'f49': '外盘 美元',
    'f55': '每股收益',
    'f161': '内盘 美元',
    'f169': '涨跌  % /100',
    'f44': '最高价 /100 美元',
    'f167': '市净率  / 100',
    'f43': '最新价  /100 美元',
    'f92': '每股净资产',
    'f46': '今开 /100 美元',
    'f116': '总市值 美元',
    'f84': '总股本',
    'f47': '成交量',
    'f171': '振幅  % /100',
    'f168': '换手率 % /100',
    'f48': '成交额',
    'f164': '市盈率 / 100  PE(ttm)',
    'f45': '最低价  /100 美元',
    'f50': '量比  /100 ',
    'f170': '涨幅  % /100'
}

# 列表页字段
list_key_map = {
    "f12": "instrument",
    "f2": "最新价",
    "f3": "涨跌幅",
    "f4": "涨跌额",
    "f5": "成交量",
    "f7": "振幅(%)",
    "f8": "换手率(%)",
    "f9": "市盈率",
    "f10": "量比",
    'f14': 'name_en',
    "f15": "最高价",
    "f16": "最低价",
    "f17": "开盘价",
    "f18": "昨收",
    "f20": "市值",  # 美元
    "f21": "市值",  # 美元
    "f23": "市净率",
    "f115": "市盈率",
}