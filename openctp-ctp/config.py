# @Project: https://github.com/Jedore/ctp.examples
# @File:    base.py
# @Time:    03/06/2024 21:38
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

# 配置了 SimNow 常用的四个环境
# 可以使用监控平台 http://openctp.cn 查看前置服务是否正常
# 也可以按需配置其他的支持 ctp官方ctpapi库的柜台
# 注意需要同时修改相应的 user/password/broker_id/authcode/appid 等信息
# 账户需要到 SimNow 官网申请 https://www.simnow.com.cn/

# SimNow 提供的四个环境
envs = {
    # 7x24环境
    "7x24": {
        "td": "tcp://182.254.243.31:40001",
        "md": "tcp://182.254.243.31:40011",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "0000000000000000",
        "appid": "simnow_client_test",
        "user_product_info": "",
    },
    # 仿真环境 第一组
    "simu1": {
        "td": "tcp://182.254.243.31:30001",
        "md": "tcp://182.254.243.31:30011",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "0000000000000000",
        "appid": "simnow_client_test",
        "user_product_info": "",
    },
    # 仿真环境 第二组
    "simu2": {
        "td": "tcp://182.254.243.31:30002",
        "md": "tcp://182.254.243.31:30012",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "0000000000000000",
        "appid": "simnow_client_test",
        "user_product_info": "",
    },
    # 仿真环境 第三组
    "simu3": {
        "td": "tcp://182.254.243.31:30003",
        "md": "tcp://182.254.243.31:30013",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "0000000000000000",
        "appid": "simnow_client_test",
        "user_product_info": "",
    },
}
