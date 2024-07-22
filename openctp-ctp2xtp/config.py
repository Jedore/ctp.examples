# @Project: https://github.com/Jedore/ctp.examples
# @File:    config.py
# @Time:    21/07/2024 22:08
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

# 在中泰官网注册申请测试账号 https://xtp.zts.com.cn/

envs = {
    # 模拟环境, 7x24运行，定时结算
    "test": {
        "td": "tcp://122.112.139.0:6102",
        "md": "tcp://119.3.103.38:6002",
        "user_id": "",
        "password": "",
        "broker_id": "",
        "authcode": "1",
        "appid": "",
    },
}
