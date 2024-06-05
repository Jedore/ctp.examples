# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryExchange.py
# @Time:    05/06/2024 22:47
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询交易所
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/
        """

        self.print("请求查询交易所")
        req = tdapi.CThostFtdcQryExchangeField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        self._check_req(req, self._api.ReqQryExchange(req, 0))

    def OnRspQryExchange(self, pExchange: tdapi.CThostFtdcExchangeField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                         nRequestID: int, bIsLast: bool):
        """ 请求查询交易所响应 """

        self._check_rsp(pRspInfo, pExchange, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
