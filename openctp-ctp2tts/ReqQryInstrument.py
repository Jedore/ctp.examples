# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrument.py
# @Time:    21/07/2024 14:42
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询合约
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENT/
        """

        self.print("请求查询合约")
        req = tdapi.CThostFtdcQryInstrumentField()
        # 一个都不填，查询全部合约
        # req.InstrumentID = "AP410"
        # req.ExchangeID = "CFFEX"
        # req.ExchangeInstID = "TS2503" # 不可过滤
        # req.ProductID = "zn"  # 不可过滤
        self._check_req(req, self._api.ReqQryInstrument(req, 0))

    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                           nRequestID: int, bIsLast: bool):
        """ 请求查询合约响应 """

        self._check_rsp(pRspInfo, pInstrument, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
