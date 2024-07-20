# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryContractBank.py
# @Time:    05/06/2024 22:53
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询签约银行
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQQRYCONTRACTBANK
        """

        # SimNow 不支持，需要实盘测验
        self.print("请求查询签约银行")
        req = tdapi.CThostFtdcQryContractBankField()
        req.BrokerID = self._broker_id
        # req.BankID = '9' # 不传则查询所有签约银行
        self._check_req(req, self._api.ReqQryContractBank(req, 0))

    def OnRspQryContractBank(self, pContractBank: tdapi.CThostFtdcContractBankField,
                             pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询签约银行响应 """

        self._check_rsp(pRspInfo, pContractBank, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
