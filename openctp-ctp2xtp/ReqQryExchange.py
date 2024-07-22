# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryExchange.py
# @Time:    21/07/2024 22:08
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询交易所
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYEXCHANGE/
        """

        self.print("请求查询交易所")
        req = tdapi.CThostFtdcQryExchangeField()
        # req.ExchangeID = "SHFE" # 不传查全部
        self._check_req(req, self._api.ReqQryExchange(req, 0))

    def OnRspQryExchange(self, pExchange: tdapi.CThostFtdcExchangeField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                         nRequestID: int, bIsLast: bool):
        """ 请求查询交易所响应 """

        self._check_rsp(pRspInfo, pExchange, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
