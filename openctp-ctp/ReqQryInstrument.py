# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInstrument.py
# @Time:    05/06/2024 22:02
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询合约
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENT/
        """

        self.print("请求查询合约")
        req = tdapi.CThostFtdcQryInstrumentField()
        # 以下四个条件均可单独作为过滤条件，返回满足所有条件的合约
        # 一个都不填，查询全部合约
        # req.InstrumentID = "AP410"
        req.ExchangeID = "CFFEX"
        # req.ExchangeInstID = "zn2504"
        # req.ProductID = "zn"
        self._check_req(req, self._api.ReqQryInstrument(req, 0))

    def OnRspQryInstrument(self, pInstrument: tdapi.CThostFtdcInstrumentField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                           nRequestID: int, bIsLast: bool):
        """ 请求查询产品响应 """

        self._check_rsp(pRspInfo, pInstrument, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
