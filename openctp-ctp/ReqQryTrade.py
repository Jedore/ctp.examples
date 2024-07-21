# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryTrade.py
# @Time:    05/06/2024 21:56
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询成交
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADE/
        """

        self.print("请求查询成交")
        req = tdapi.CThostFtdcQryTradeField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # 以下条件均可单独作为过滤条件，一个都不填，查询全部成交
        # req.InstrumentID = "ao2408"
        # req.ExchangeID = "SHFE"
        # req.TradeID = "         402"
        # req.TradeTimeStart = "17:00:49"
        # req.TradeTimeEnd = "17:00:42"
        self._check_req(req, self._api.ReqQryTrade(req, 0))

    def OnRspQryTrade(self, pTrade: tdapi.CThostFtdcTradeField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                      nRequestID: int, bIsLast: bool):
        """ 请求查询成交响应 """

        self._check_rsp(pRspInfo, pTrade, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
