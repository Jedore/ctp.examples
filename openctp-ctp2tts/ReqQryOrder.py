# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryOrder.py
# @Time:    21/07/2024 14:42
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询报单
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYORDER/
        """

        self.print("请求查询报单")
        req = tdapi.CThostFtdcQryOrderField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.InstrumentID = "AP410"
        # req.ExchangeID = "SHFE"
        # req.OrderSysID = "" # 不可过滤
        # req.InsertTimeStart = ""  # HH:MM:SS 不可过滤
        # req.InsertTimeEnd = ""  # 不可过滤
        self._check_req(req, self._api.ReqQryOrder(req, 0))

    def OnRspQryOrder(self, pOrder: tdapi.CThostFtdcOrderField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                      nRequestID: int, bIsLast: bool):
        """ 请求查询报单响应 """

        self._check_rsp(pRspInfo, pOrder, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
