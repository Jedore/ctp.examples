# @Project: https://github.com/Jedore/ctp.examples
# @File:    base.py
# @Time:    03/06/2024 21:38
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

# 配置了 SimNow 常用的四个环境
# 可以使用监控平台 http://openctp.cn 查看前置服务是否正常
# 也可以按需配置其他的支持 ctp官方ctpapi库的柜台
# 注意需要同时修改相应的 user/password/broker_id/authcode/appid 等信息

# SimNow 提供的四个环境
fronts = {
    "7x24": {
        "td": "tcp://180.168.146.187:10130",
        "md": "tcp://180.168.146.187:10131",
    },
    "电信1": {
        "td": "tcp://180.168.146.187:10201",
        "md": "tcp://180.168.146.187:10211",
    },
    "电信2": {
        "td": "tcp://180.168.146.187:10202",
        "md": "tcp://180.168.146.187:10212",
    },
    "移动": {
        "td": "tcp://218.202.237.33:10203",
        "md": "tcp://218.202.237.33:10213",
    },
}

# 在SimNow申请的 投资者ID / 密码
user_id = "xxx"
password = "xxx"

# 以下是连接 SimNow 环境的固定值
broker_id = "9999"
authcode = "0000000000000000"
appid = "simnow_client_test"
user_product_info = ''
