# openctp-ctp2tora examples

使用 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 连接 openctp [华鑫证券奇点柜台](https://github.com/openctp/openctp/tree/master/ctp2STP)

## 快速上手

### 说明

提供了 以下 行情API 和 交易API 的多个接口代码示例。

`config.py` 是配置文件

`base_mdapi.py` 是行情API基类文件，可指定行情前置地址, 包了连接、登录 等基本逻辑

`base_tdapi.py` 是交易API基类文件，可指定交易前置地址, 包了连接、认证、登录 等基本逻辑

其他 `py` 文件均包含了一个具体的业务接口

除了 `config.py`, 其他 `py` 文件均可直接运行

### 使用

- 准备 Python 环境 (3.7 ~ 3.12)
-
安装 [openctp-ctp](https://github.com/openctp/openctp-ctp-python)  [openctp-ctp-channels](https://github.com/Jedore/openctp-ctp-channels)
```bash
pip install openctp-ctp==6.7.2.*
pip install openctp-ctp-channels
```
- 克隆仓库
    ```bash
    git clone https://github.com/Jedore/ctp.examples.git
    cd ctp.examples/openctp-ctp2tora
    ```
- 修改用户名/密码

  config.py

- 指定环境

  base_mdapi.py / base_tdapi.py

- 将 openctp-ctp 切换为 tora 通道

  ```bash 
  openctp-channels switch tora
  ``` 
- 运行示例
  ```bash
  $ python base_tdapi.py
  >>>>  启动交易Api
   [2024-07-22 14:37:59.692308]
   投资者: 00578417
   API版本: V6_6_1_P1
   交易前置地址: tcp://210.14.72.21:4400
  >>>>  交易前置连接成功
   [2024-07-22 14:37:59.790752]
  >>>>  客户端认证请求
   [2024-07-22 14:37:59.790752]
   发送请求: AppID=,AuthCode=,BrokerID=,UserID=00578417,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: AppID=,AppType=,BrokerID=,UserID=00578417,UserProductInfo=
  >>>>  用户登录请求
   [2024-07-22 14:37:59.791753]
   发送请求: BrokerID=,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=00578417,UserProductInfo=
   初始化完成
   响应成功: ErrorID=0, ErrorMsg=VIP:正确
   响应内容: BrokerID=,CZCETime=14:37:59,DCETime=14:37:59,FFEXTime=14:37:59,FrontID=1001,INETime=14:37:59,LoginTime=,MaxOrderRef=1,SHFETime=14:37:59,SessionID=-1423039366,SystemName=StockVIP,TradingDay=20240722,UserID=00578417
   ---
   交易日: 20240722
   交易系统名称: StockVIP
  ```

## 行情API

- [x] 用户登录请求
- [x] 订阅行情

## 交易API

- [x] 客户端认证请求
- [x] 用户登录请求
- [x] 请求查询报单
- [x] 请求查询成交
- [x] 请求查询合约
- [x] 请求查询交易所

## 其他

- [ ] k线合成