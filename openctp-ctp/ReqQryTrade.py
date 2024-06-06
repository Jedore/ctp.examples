# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryTrade.py
# @Time:    05/06/2024 21:56
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询成交
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADE/
        """

        self.print("请求查询成交")
        req = tdapi.CThostFtdcQryTradeField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # todo
        # req.InstrumentID = ""
        # req.ExchangeID = ""
        # req.TradeID = ""
        # req.TradeTimeStart = ""
        # req.TradeTimeEnd = ""
        self._check_req(req, self._api.ReqQryTrade(req, 0))

    def OnRspQryTrade(self, pTrade: tdapi.CThostFtdcTradeField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                      nRequestID: int, bIsLast: bool):
        """ 请求查询成交响应 """

        self._check_rsp(pRspInfo, pTrade, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
