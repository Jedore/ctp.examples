# @Project: https://github.com/Jedore/ctp.examples
# @File:    config.py
# @Time:    21/07/2024 22:08
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

# 需要申请账户 https://www.n-sight.com.cn/
# 貌似普通账户不能使用 7x24环境，专业账户才可以

envs = {
    "7x24": {
        "td": "tcp://210.14.72.16:9500",
        "md": "tcp://210.14.72.16:9402",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "",
        "appid": "",
    },
    # 仿真环境
    "simu": {
        "td": "tcp://210.14.72.21:4400",
        "md": "tcp://210.14.72.21:4402",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "",
        "appid": "",
    },
}
