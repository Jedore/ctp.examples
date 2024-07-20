# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrumentOrderCommRate.py
# @Time:    05/06/2024 22:45
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询报单手续费
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTORDERCOMMRATE/
        """

        self.print("请求查询报单手续费")
        req = tdapi.CThostFtdcQryInstrumentOrderCommRateField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        req.InstrumentID = "TS2412"  # 很多合约没有报单手续费，返回None
        self._check_req(req, self._api.ReqQryInstrumentOrderCommRate(req, 0))

    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate: tdapi.CThostFtdcInstrumentOrderCommRateField,
                                        pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询合约报单手续费率响应 """

        self._check_rsp(pRspInfo, pInstrumentOrderCommRate, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
