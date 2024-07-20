# @Project: https://github.com/Jedore/ctp.examples
# @File:    base_tdapi.py
# @Time:    03/06/2024 21:38
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

import inspect
import os.path
import sys
import time
from datetime import datetime as dt

from openctp_ctp import tdapi

import config


class CTdSpiBase(tdapi.CThostFtdcTraderSpi):

    def __init__(self, conf=config.envs["7x24"]):
        super().__init__()

        self.print("启动交易Api")
        self._front = conf.get("td")
        self._user_id = conf.get("user_id")
        self._password = conf.get("password")
        self._authcode = conf.get("authcode")
        self._appid = conf.get("appid")
        self._broker_id = conf.get("broker_id")
        self._user_product_info = conf.get("user_product_info")

        self._is_login = False
        self._is_last = False
        self._trading_day = ""

        self._front_id = None
        self._session_id = None

        flat_dir = self._user_id + "_td"
        if not os.path.exists(flat_dir):
            os.mkdir(flat_dir)
        flat_path = os.path.join(flat_dir, self._user_id)

        self._api: tdapi.CThostFtdcTraderApi = tdapi.CThostFtdcTraderApi.CreateFtdcTraderApi(flat_path)

        print(" 投资者:", self._user_id)
        print(" API版本:", self._api.GetApiVersion())
        print(" 交易前置地址:", self._front)

        # 注册交易前置
        self._api.RegisterFront(self._front)
        # 注册交易回调实例
        self._api.RegisterSpi(self)
        # 订阅私有流
        self._api.SubscribePrivateTopic(tdapi.THOST_TERT_QUICK)
        # 订阅公有流
        self._api.SubscribePublicTopic(tdapi.THOST_TERT_QUICK)
        # 初始化交易实例
        self._api.Init()

        print(" 初始化完成")

        self.wait_login()

    @property
    def is_login(self):
        return self._is_login

    def __del__(self):
        # 释放实例
        self._api.Release()

    @staticmethod
    def _check_req(req, ret: int):
        """检查请求"""

        # 打印请求
        params = []
        for name, value in inspect.getmembers(req):
            # 输出所有首字母大写的字段
            if name[0].isupper():
                # 过滤密码字段
                if 'Password' in name:
                    continue
                params.append(f"{name}={value}")
        print(" 发送请求:", ",".join(params))

        # 检查请求结果
        error = {
            0: "成功",
            -1: "网络连接失败",
            -2: "未处理请求超过许可数",
            -3: "每秒发送请求数超过许可数",
        }.get(ret, "未知错误")
        if ret != 0:
            print(f" 请求失败: {ret}={error}")

    def _check_rsp(self, pRspInfo: tdapi.CThostFtdcRspInfoField, rsp=None, is_last: bool = True) -> bool:
        """检查响应

        :return: True: 成功   False: 失败
        """

        self._is_last = is_last

        if pRspInfo and pRspInfo.ErrorID != 0:
            print(f" 响应失败: ErrorID={pRspInfo.ErrorID}, ErrorMsg={pRspInfo.ErrorMsg}")
            return False

        if pRspInfo:
            print(f" 响应成功: ErrorID={pRspInfo.ErrorID}, ErrorMsg={pRspInfo.ErrorMsg}")
        # else:
        #     print(f" 响应成功: pRspInfo is None")

        if rsp:
            params = []
            for name, value in inspect.getmembers(rsp):
                # 输出所有首字母大写的字段
                if name[0].isupper():
                    params.append(f"{name}={value}")
            print(" 响应内容:", ",".join(params))
        else:
            print(" 响应内容: None")

        return True

    @staticmethod
    def _print_rtn(rsp_rtn, prefix: str = "", pRspInfo: tdapi.CThostFtdcRspInfoField = None):
        if rsp_rtn:
            params = []
            for name, value in inspect.getmembers(rsp_rtn):
                if name[0].isupper():
                    params.append(f"{name}={value}")
            print(f" {prefix}:", ",".join(params))
            if pRspInfo:
                print(f"\tErrorID={pRspInfo.ErrorID}, ErrorMsg={pRspInfo.ErrorMsg}")

    @staticmethod
    def print(*args, **kwargs):
        print(">>>> ", *args, **kwargs)
        print(dt.now().strftime(" [%Y-%m-%d %H:%M:%S.%f]"))

    def OnFrontConnected(self):
        """交易前置连接成功"""
        self.print("交易前置连接成功")

        self.print("客户端认证请求")

        req = tdapi.CThostFtdcReqAuthenticateField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.AppID = self._appid
        req.AuthCode = self._authcode
        req.UserProductInfo = self._user_product_info
        self._check_req(req, self._api.ReqAuthenticate(req, 0))

    def OnFrontDisconnected(self, nReason: int):
        """交易前置连接断开"""
        self.print("交易前置连接断开: nReason=", nReason)

    def OnRspAuthenticate(self, pRspAuthenticateField: tdapi.CThostFtdcRspAuthenticateField,
                          pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 客户端认证响应 """
        if not self._check_rsp(pRspInfo, pRspAuthenticateField):
            return

        self.print("用户登录请求")
        # 登录
        req = tdapi.CThostFtdcReqUserLoginField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.Password = self._password
        req.UserProductInfo = self._user_product_info
        if sys.platform == "darwin":
            # Mac
            self._check_req(req, self._api.ReqUserLogin(req, 0, 0, ""))
        else:
            # Linux/Windows
            self._check_req(req, self._api.ReqUserLogin(req, 0))

    def OnRspUserLogin(self, pRspUserLogin: tdapi.CThostFtdcRspUserLoginField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                       nRequestID: int, bIsLast: bool):
        """ 登录请求响应 """
        if not self._check_rsp(pRspInfo, pRspUserLogin):
            return

        self._trading_day = pRspUserLogin.TradingDay
        self._front_id = pRspUserLogin.FrontID
        self._session_id = pRspUserLogin.SessionID
        self._is_login = True

        print(" ---")
        print(" 交易日:", self._trading_day)
        print(" 交易系统名称:", pRspUserLogin.SystemName)
        print(" 后台版本信息:", pRspUserLogin.SysVersion)

    def wait_login(self):
        # 登录成功后继续
        while True:
            time.sleep(1)
            if self.is_login:
                break

    def wait_last(self):
        while True:
            time.sleep(1)
            if self._is_last:
                break
        input("\n\n Enter any key to exit ...\n")


if __name__ == "__main__":
    spi = CTdSpiBase()

    spi.wait_last()
