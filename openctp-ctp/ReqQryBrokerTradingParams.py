# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryBrokerTradingParams.py
# @Time:    06/06/2024 21:00
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询经纪公司交易参数
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGPARAMS/
        """

        self.print("请求查询经纪公司交易参数")
        req = tdapi.CThostFtdcQryBrokerTradingParamsField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.CurrencyID = "CNY"
        self._check_req(req, self._api.ReqQryBrokerTradingParams(req, 0))

    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams: tdapi.CThostFtdcBrokerTradingParamsField,
                                    pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询经纪公司交易参数响应 """

        self._check_rsp(pRspInfo, pBrokerTradingParams, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
