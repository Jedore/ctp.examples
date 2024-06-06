# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryAccountregister.py
# @Time:    06/06/2024 21:26
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 请求查询银期签约关系
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYACCOUNTREGISTER/
        """

        # SimNow 不支持，需要实盘测验
        self.print("请求查询银期签约关系")
        req = tdapi.CThostFtdcQryAccountregisterField()
        self._check_req(req, self._api.ReqQryAccountregister(req, 0))

    def OnRspQryAccountregister(self, pAccountregister: tdapi.CThostFtdcAccountregisterField,
                                pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询银期签约关系响应 """

        self._check_rsp(pRspInfo, pAccountregister, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
