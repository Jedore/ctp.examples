# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrumentCommissionRate.py
# @Time:    05/06/2024 22:32
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询合约手续费率
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTCOMMISSIONRATE/
        """

        self.print("请求查询合约手续费率")
        req = tdapi.CThostFtdcQryInstrumentCommissionRateField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        req.InstrumentID = "AP410"  # 若不传，则返回持仓合约的手续费率;
        self._check_req(req, self._api.ReqQryInstrumentCommissionRate(req, 0))

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate: tdapi.CThostFtdcInstrumentCommissionRateField,
                                         pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询合约手续费率响应 """

        self._check_rsp(pRspInfo, pInstrumentCommissionRate, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
