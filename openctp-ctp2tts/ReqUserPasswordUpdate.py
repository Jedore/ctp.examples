# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqUserPasswordUpdate.py
# @Time:    21/07/2024 14:42
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 用户口令更新请求
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/
        """

        self.print("用户口令更新请求")
        req = tdapi.CThostFtdcUserPasswordUpdateField()
        req.BrokerID = self._broker_id
        req.UserID = self._user_id
        req.OldPassword = ''  # 旧口令
        req.NewPassword = ''  # 新口令
        self._check_req(req, self._api.ReqUserPasswordUpdate(req, 0))

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate: tdapi.CThostFtdcUserPasswordUpdateField,
                                pRspInfo: tdapi.CThostFtdcRspInfoField,
                                nRequestID: int, bIsLast: bool):
        """ 用户口令更新请求响应 """

        self._check_rsp(pRspInfo, pUserPasswordUpdate, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
