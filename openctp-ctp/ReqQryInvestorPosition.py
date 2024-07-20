# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInvestorPosition.py
# @Time:    05/06/2024 21:44
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询投资者
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITION/
        """

        self.print("请求查询投资者持仓")
        req = tdapi.CThostFtdcQryInvestorPositionField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.InstrumentID = 'AP410'  # 不填合约查全部
        self._check_req(req, self._api.ReqQryInvestorPosition(req, 0))

    def OnRspQryInvestorPosition(self, pInvestorPosition: tdapi.CThostFtdcInvestorPositionField,
                                 pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询投资者响应 """
        self._check_rsp(pRspInfo, pInvestorPosition, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
