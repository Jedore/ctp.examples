# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryTradingCode.py
# @Time:    05/06/2024 22:22
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询交易编码
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADINGCODE/
        """

        # SimNow 7x24的数据 BizType 貌似有问题
        self.print("请求查询交易编码")
        req = tdapi.CThostFtdcQryTradingCodeField()
        # todo 交易编码有用吗？ 不传; BrokerID,InvestorID; BrokerID; InvestorID 多种情况应答不一致
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.ExchangeID = "CZCE"
        self._check_req(req, self._api.ReqQryTradingCode(req, 0))

    def OnRspQryTradingCode(self, pTradingCode: tdapi.CThostFtdcTradingCodeField,
                            pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询交易编码响应 """

        self._check_rsp(pRspInfo, pTradingCode, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
