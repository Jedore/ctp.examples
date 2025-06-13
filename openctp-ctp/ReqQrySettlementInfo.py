# @Project: https://github.com/Jedore/ctp.examples
# @File:    ReqQrySettlementInfoo.py
# @Time:    03/06/2024 21:38
# @Author:  Jedore
# @Email:   jedorefight@gmail.com
# @Addr:    https://github.com/Jedore

from base_tdapi import CTdSpiBase, tdapi


class CTdSpi(CTdSpiBase):
    def __init__(self):
        super().__init__()

        self.content = b""

    def req(self):
        """ 请求查询投资者结算结果
        doc: https://ctpdoc.jedore.top/6.6.9/JYJK/CTHOSTFTDCTRADERSPI/REQQRYSETTLEMENTINFO/
        """

        self.print("请求查询投资者结算结果")
        # 可以查询当天或历史结算单，也可以查询月结算单，但是前提是CTP柜台生成了相应的日或月结算单。
        req = tdapi.CThostFtdcQrySettlementInfoField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user_id
        # req.TradingDay = ""  # 交易日 日结算单: yymmdd, 月结算单: yymm
        self._check_req(req, self._api.ReqQrySettlementInfo(req, 0))

    def OnRspQrySettlementInfo(self, pSettlementInfo: tdapi.CThostFtdcSettlementInfoField,
                               pRspInfo: tdapi.CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """ 请求查询投资者结算结果响应 """

        if pRspInfo and pRspInfo.ErrorID:
            print(f"请求查询投资者结算结果响应失败: ErrorID={pRspInfo.ErrorID} ErrorMsg={pRspInfo.ErrorMsg}")
            return

        if not bIsLast:
            if pSettlementInfo:
                self.content += pSettlementInfo.Content
        if bIsLast:
            if pSettlementInfo:
                self.content += pSettlementInfo.Content
            print(self.content.decode("gbk"))
            self.content = b""


if __name__ == '__main__':
    spi = CTdSpi()
    spi.req()

    spi.wait_last()
