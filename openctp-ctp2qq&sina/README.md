# openctp-ctp2qq&sina examples

## 快速上手

### 说明

提供了 以下 行情API接口代码示例。

`config.py` 是配置文件

`base_mdapi.py` 是行情API基类文件，可指定行情前置地址, 包了连接、登录 等基本逻辑

除了 `config.py`, 其他 `py` 文件均可直接运行

### 使用

- 准备 Python 环境 (3.7 ~ 3.14)
- 安装 [openctp-ctp](https://github.com/openctp/openctp-ctp-python)  [openctp-ctp-channels](https://github.com/Jedore/openctp-ctp-channels)
- 克隆仓库
    ```bash
    git clone https://github.com/Jedore/ctp.examples.git
    cd ctp.examples/openctp-ctp2qq&sina
    ```

- 运行示例
  ```bash
  $ python SubscribeMarketData.py
  >>>>  启动行情Api
   [2024-10-09 13:05:07.115474]
   投资者:
   API版本: V6_7_7
   初始化完成
  >>>>  行情前置连接成功
   [2024-10-09 13:05:07.119475]
  >>>>  用户登录请求
   [2024-10-09 13:05:07.119475]
   发送请求: BrokerID=,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: BrokerID=,CZCETime=,DCETime=,FFEXTime=,FrontID=0,GFEXTime=,INETime=,LoginTime=,MaxOrderRef=,SHFETime=,SessionID=0,SysVersion=,SystemName=,TradingDay=,UserID=
   ---
   交易日:
   交易系统名称:
   后台版本信息:
   FrontID: 0
   SessionID: 0
  >>>>  订阅行情
   [2024-10-09 13:05:08.119932]
   发送请求: 600000,000001,00700,AAPL


   Enter any key to exit ...
   行情通知: ActionDay=20241009,AskPrice1=12.14,AskPrice2=12.15,AskPrice3=12.16,AskPrice4=12.17,AskPrice5=12.18,AskVolume1=77700,AskVolume2=235100,AskVolume3=35700,AskVolume4=134400
  ,AskVolume5=360236,AveragePrice=0.0,BandingLowerPrice=0.0,BandingUpperPrice=0.0,BidPrice1=12.13,BidPrice2=12.12,BidPrice3=12.11,BidPrice4=12.1,BidPrice5=12.09,BidVolume1=23200,Bid
  Volume2=129000,BidVolume3=66900,BidVolume4=25900,BidVolume5=25500,ClosePrice=0.0,CurrDelta=0.0,ExchangeID=SZSE,ExchangeInstID=000001,HighestPrice=12.63,InstrumentID=000001,LastPri
  ce=12.13,LowerLimitPrice=0.0,LowestPrice=11.74,OpenInterest=0.0,OpenPrice=12.63,PreClosePrice=12.88,PreDelta=0.0,PreOpenInterest=0.0,PreSettlementPrice=0.0,SettlementPrice=0.0,TradingDay=20241009,Turnover=3518230343.26,UpdateMillisec=0,UpdateTime=13:04:51,UpperLimitPrice=0.0,Volume=288498599
  ```

## 行情API

- [x] 用户登录请求
- [x] 订阅行情

## 其他

- [ ] k线合成