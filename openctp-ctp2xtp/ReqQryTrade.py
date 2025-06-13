# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryTrade.py
# @Time:    22/07/2024 14:01
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询成交
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADE/
        """

        self.print("请求查询成交")
        req = tdapi.CThostFtdcQryTradeField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.InstrumentID = ""  # 可过滤
        # req.ExchangeID = "DCE"  # 可过滤
        # req.TradeID = "" # 不可作为过滤条件
        # req.TradeTimeStart = ""  # HH:MM:SS  不可过滤
        # req.TradeTimeEnd = ""  # HH:MM:SS  不可过滤
        self._check_req(req, self._api.ReqQryTrade(req, 0))

    def OnRspQryTrade(self, pTrade: tdapi.CThostFtdcTradeField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                      nRequestID: int, bIsLast: bool):
        """ 请求查询成交响应 """

        self._check_rsp(pRspInfo, pTrade, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
