# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryTradingCode.py
# @Time:    05/06/2024 22:22
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询交易编码
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADINGCODE/
        """

        self.print("请求查询交易编码")
        req = tdapi.CThostFtdcQryTradingCodeField()
        # todo 交易编码有用吗？ 不传; BrokerID,InvestorID; BrokerID; InvestorID 多种情况应答不一致
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.ExchangeID = "SHFE"
        self._check_req(req, self._api.ReqQryTradingCode(req, 0))

    def OnRspQryTradingCode(self, pTradingCode: tdapi.CThostFtdcTradingCodeField,
                            pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询交易编码响应 """

        self._check_rsp(pRspInfo, pTradingCode, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
