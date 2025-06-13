# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqFromFutureToBankByFuture.py
# @Time:    06/06/2024 21:16
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 期货发起期货资金转银行请求
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQFROMFUTURETOBANKBYFUTURE/
        """

        # SimNow 不支持，需要实盘测验
        self.print("期货发起期货资金转银行请求")
        req = tdapi.CThostFtdcReqTransferField()
        req.TradeCode = "202001"  # 业务功能码: 期货发起期货资金转银行
        req.BankID = "11"  # 银行编码 (通过查询签约银行可以获取银行编码)
        req.BankBranchID = "0000"  # (通过查询签约银行可以获取银行编码)
        req.BrokerID = self._broker_id
        req.LastFragment = tdapi.THOST_FTDC_LF_Yes
        req.IdCardType = tdapi.THOST_FTDC_CFT_Passport
        req.CustType = tdapi.THOST_FTDC_CUSTT_Person
        req.BankAccount = ""  # 银行账号, 必填
        req.BankPassWord = ""  # 银行密码, 必填
        req.Password = ""  # 期货账户 资金密码(默认身份证后6位), 必填
        req.AccountID = self._user_id  # 投资者ID
        req.InstallID = 1
        req.FutureSerial = 0
        req.VerifyCertNoFlag = tdapi.THOST_FTDC_YNI_No
        req.CurrencyID = "CNY"  # 币种
        req.TradeAmount = 1  # 转账金额(元)
        req.FutureFetchAmount = 0
        req.CustFee = 0
        req.BrokerFee = 0
        req.SecuPwdFlag = tdapi.THOST_FTDC_BPWDF_BlankCheck
        req.TID = 0
        self._check_req(req, self._api.ReqFromFutureToBankByFuture(req, 0))

    def OnRspFromFutureToBankByFuture(self, pReqTransfer: tdapi.CThostFtdcReqTransferField,
                                      pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 期货发起期货资金转银行请求 错误响应 """

        self._check_rsp(pRspInfo, pReqTransfer, is_last=bIsLast)

    def OnRtnFromBankToFutureByBank(self, pRspTransfer: tdapi.CThostFtdcRspTransferField):
        """ 期货发起期货资金转银行请求通知 """
        self._print_rtn(pRspTransfer, "期货发起期货资金转银行请求通知")


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
