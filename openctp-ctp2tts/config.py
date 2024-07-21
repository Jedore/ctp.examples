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
        "td": "tcp://121.37.80.177:20002",
        "md": "tcp://121.37.80.177:20004",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
    # 仿真
    "simu": {
        "td": "tcp://121.37.90.193:20002",
        "md": "",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
    # 仿真vip
    "simu-vip": {
        "td": "tcp://42.192.226.242:20002",
        "md": "",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "",
        "appid": "",
        "user_product_info": "",
    },
}
