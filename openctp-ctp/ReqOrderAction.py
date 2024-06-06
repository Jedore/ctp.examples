# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqOrderAction.py
# @Time:    06/06/2024 22:22
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 报单操作请求
        doc: 
        """

        self.print("报单操作请求")
        req = tdapi.CThostFtdcInputOrderActionField()
        # todo
        self._check_req(req, self._api.ReqOrderAction(req, 0))

    def OnRspQryInvestor(self, pInvestor: tdapi.CThostFtdcInvestorField, pRspInfo: tdapi.CThostFtdcRspInfoField,
                         nRequestID: int, bIsLast: bool):
        """ 请求响应 """

        self._check_rsp(pRspInfo, pInvestor, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
