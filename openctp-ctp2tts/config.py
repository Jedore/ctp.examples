# @Project: https://github.com/Jedore/ctp.examples
# @File:    config.py
# @Time:    21/07/2024 14:29
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

# 可以使用监控平台 http://openctp.cn 查看前置服务是否正常
# 账户需要到 openctp 公众号, 发送"注册"

# TTS 提供的环境
envs = {
    "7x24": {
        "td": "tcp://724.openctp.cn:30001",
        "md": "tcp://724.openctp.cn:30011",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
    # 仿真
    "simu": {
        "td": "tcp://trading.openctp.cn:30002",
        "md": "",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
    # 仿真vip
    "simu-vip": {
        "td": "tcp://vip.openctp.cn:30003",
        "md": "",
        "user_id": "",
        "password": "",
        "broker_id": "9999",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
}
