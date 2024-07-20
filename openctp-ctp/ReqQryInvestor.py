# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQrySettlementInfoo.py
# @Time:    03/06/2024 21:38
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询投资者
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTOR/
        """

        self.print("请求查询投资者")
        req = tdapi.CThostFtdcQryInvestorField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        self._check_req(req, self._api.ReqQryInvestor(req, 0))

    def OnRspQryInvestor(self, pInvestor: tdapi.CThostFtdcInvestorField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                         nRequestID: int, bIsLast: bool):
        """ 请求查询投资者响应 """

        self._check_rsp(pRspInfo, pInvestor, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
