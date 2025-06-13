# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQryInvestorPositionDetail.py
# @Time:    21/07/2024 14:42
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):

    def req(self):
        """ 请求查询投资者持仓明细
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITIONDETAIL/
        """

        # CTP系统根据来自交易所的成交记录生成持仓明细记录，一笔成交记录对应一条持仓明细记录。
        self.print("请求查询投资者持仓明细")
        req = tdapi.CThostFtdcQryInvestorPositionDetailField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.InstrumentID = 'CF407'  # 不传则查所有持仓
        self._check_req(req, self._api.ReqQryInvestorPositionDetail(req, 0))

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail: tdapi.CThostFtdcInvestorPositionDetailField,
                                       pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询投资者持仓明细响应 """

        self._check_rsp(pRspInfo, pInvestorPositionDetail, is_last=bIsLast)


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
