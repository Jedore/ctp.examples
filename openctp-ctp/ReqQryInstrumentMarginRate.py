# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrumentMarginRate.py
# @Time:    05/06/2024 22:39
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询合约保证金率
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTMARGINRATE/
        """

        self.print("请求查询合约保证金率")
        req = tdapi.CThostFtdcQryInstrumentMarginRateField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        req.HedgeFlag = tdapi.THOST_FTDC_HF_Speculation  # todo 不传好像不影响？
        req.InstrumentID = "AP410"  # 若不传，则返回持仓合约的保证金率;
        self._check_req(req, self._api.ReqQryInstrumentMarginRate(req, 0))

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate: tdapi.CThostFtdcInstrumentMarginRateField,
                                     pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求合约保证金率响应 """

        self._check_rsp(pRspInfo, pInstrumentMarginRate, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
