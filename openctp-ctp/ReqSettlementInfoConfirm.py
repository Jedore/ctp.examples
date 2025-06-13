# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqSettlementInfoConfirm.py
# @Time:    05/06/2024 22:51
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 投资者结算结果确认
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQSETTLEMENTINFOCONFIRM/
        """

        self.print("投资者结算结果确认")
        req = tdapi.CThostFtdcSettlementInfoConfirmField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        self._check_req(req, self._api.ReqSettlementInfoConfirm(req, 0))

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm: tdapi.CThostFtdcSettlementInfoConfirmField,
                                   pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 投资者结算结果确认响应 """

        self._check_rsp(pRspInfo, pSettlementInfoConfirm, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
