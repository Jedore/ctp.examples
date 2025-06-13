# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryProduct.py
# @Time:    05/06/2024 22:16
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询产品
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYPRODUCT/
        """

        self.print("请求查询产品")
        req = tdapi.CThostFtdcQryProductField()
        # 不传则查询所有产品
        # req.ProductID = "ag"

        # req.ProductClass = "1"    # 不可过滤
        # req.ExchangeID = "DCE"    # 不可过滤
        self._check_req(req, self._api.ReqQryProduct(req, 0))

    def OnRspQryProduct(self, pProduct: tdapi.CThostFtdcProductField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                        nRequestID: int, bIsLast: bool):
        """ 请求查询产品响应 """

        self._check_rsp(pRspInfo, pProduct, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
