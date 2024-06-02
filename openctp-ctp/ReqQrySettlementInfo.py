from base import CTdBase, tdapi


class CTd(CTdBase):
    def ReqQrySettlementInfo(self):
        """请求查询投资者结算结果"""
        req = tdapi.CThostFtdcQrySettlementInfoField()
        req.BrokerID = self._broker_id
        req.InvestorID = self._user
        self._check_req(req, self._api.ReqQrySettlementInfo(req, 0))

    def OnRspQrySettlementInfo(
        self,
        pSettlementInfo: tdapi.CThostFtdcSettlementInfoField,
        pRspInfo: tdapi.CThostFtdcRspInfoField,
        nRequestID: int,
        bIsLast: bool,
    ):
        """ 请求查询投资者结算结果响应 """
        if pRspInfo and pRspInfo.ErrorID:
            print("失败")
            return

        if not bIsLast:
            if pSettlementInfo:
                self.content += pSettlementInfo.Content
        if bIsLast:
            if pSettlementInfo:
                self.content += pSettlementInfo.Content
            print(self.content.decode("gbk"))
            self.content = b""
