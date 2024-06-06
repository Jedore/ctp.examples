# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqUserPasswordUpdate.py
# @Time:    06/06/2024 22:24
# @Author:  Jedore
# @Eamil:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self, *args):
        super().__init__(*args)

    def req(self):
        """ 用户口令更新请求
        doc: https://ctpapi.jedore.top/6.7.2/JYJK/CTHOSTFTDCTRADERSPI/REQUSERPASSWORDUPDATE/
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
