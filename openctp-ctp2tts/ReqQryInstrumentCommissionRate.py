# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrumentCommissionRate.py
# @Time:    21/07/2024 14:42
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
        # 若不传以下条件，则返回持仓合约的手续费率
        # req.InstrumentID = "AP410"
        # req.ExchangeID = "SHFE"  # 若单指定交易所，则返回交易所所有合约的手续费
        self._check_req(req, self._api.ReqQryInstrumentCommissionRate(req, 0))

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate: tdapi.CThostFtdcInstrumentCommissionRateField,
                                         pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询合约手续费率响应 """

        self._check_rsp(pRspInfo, pInstrumentCommissionRate, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
