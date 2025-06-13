# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqOrderAction.py
# @Time:    06/06/2024 22:22
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 报单操作请求
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/
        """

        self.print("报单撤销请求")
        self.order_cancel2('SHFE', 'ao2408', 1, -533657423, '           1')

    def order_cancel1(self, exchange_id: str, instrument_id: str, order_sys_id: str):
        """报单撤销请求 方式一

        - 错误响应: OnRspOrderAction，OnErrRtnOrderAction
        - 正确响应：OnRtnOrder
        """
        print(" 方式一")

        # 撤单请求，首先需要有一笔未成交的订单，可以使用限价单，按照未成交订单信息填写撤单请求
        req = tdapi.CThostFtdcInputOrderActionField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        req.UserID = self._user_id
        req.ExchangeID = exchange_id
        req.InstrumentID = instrument_id
        req.ActionFlag = tdapi.THOST_FTDC_AF_Delete

        req.OrderSysID = order_sys_id  # OrderSysId 字符前面的空格也要带着

        # 若成功，会通过 报单回报 返回新的订单状态, 若失败则会响应失败
        self._check_req(req, self._api.ReqOrderAction(req, 0))

    def order_cancel2(self, exchange_id: str, instrument_id: str, front_id: int, session_id: int, order_ref: str):
        """报单撤销请求 方式二

        - 错误响应: OnRspOrderAction，OnErrRtnOrderAction
        - 正确响应：OnRtnOrder
        """
        print(" 方式二")

        # 撤单请求，首先需要有一笔未成交的订单，可以使用限价单，按照未成交订单信息填写撤单请求
        req = tdapi.CThostFtdcInputOrderActionField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        req.UserID = self._user_id
        req.ExchangeID = exchange_id
        req.InstrumentID = instrument_id
        req.ActionFlag = tdapi.THOST_FTDC_AF_Delete

        req.FrontID = front_id
        req.SessionID = session_id
        req.OrderRef = order_ref  # OrderRef 字符前面的空格也要带着

        # 若成功，会通过 报单回报 返回新的订单状态, 若失败则会响应失败
        self._check_req(req, self._api.ReqOrderAction(req, 0))

    def OnRspOrderAction(self, pInputOrderAction: tdapi.CThostFtdcInputOrderActionField,
                         pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """报单操作请求响应"""
        self._check_rsp(pRspInfo, pInputOrderAction, bIsLast)

    def OnRtnOrder(self, pOrder: tdapi.CThostFtdcOrderField):
        """报单通知，当执行ReqOrderInsert后并且报出后，收到返回则调用此接口，私有流回报。"""
        self._print_rtn(pOrder, f'报单通知[{pOrder.StatusMsg}]')
        print(f"\tOrderSysID={pOrder.OrderSysID}, FrontID={pOrder.FrontID}, "
              f"SessionID={pOrder.SessionID}, OrderRef={pOrder.OrderRef}")


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
