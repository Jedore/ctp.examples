# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqOrderInsert.py
# @Time:    06/06/2024 22:21
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 报单录入请求
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/
        """

        self.print("报单录入请求")
        req = tdapi.CThostFtdcInputOrderField()
        # todo
        self._check_req(req, self._api.ReqOrderInsert(req, 0))

    def OnRspQryInvestor(self, pInvestor: tdapi.CThostFtdcInvestorField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                         nRequestID: int, bIsLast: bool):
        """ 请求响应 """

        self._check_rsp(pRspInfo, pInvestor, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
