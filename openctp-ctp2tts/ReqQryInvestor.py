# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQrySettlementInfoo.py
# @Time:    21/07/2024 14:42
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询投资者
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTOR/
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
