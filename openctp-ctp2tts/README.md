# openctp-ctp2tts examples

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
    cd ctp.examples/openctp-ctp2tts
    ```
- 修改用户名/密码

  config.py

- 指定环境

  base_mdapi.py / base_tdapi.py

- 将 openctp-ctp 切换为 tts 通道

  ```bash 
  openctp-channels switch tts
  ``` 
- 运行示例
  ```bash
  $ python base_tdapi.py
  >>>>  启动交易Api
   [2024-07-21 16:43:56.932012]
   投资者: 4645
   API版本: V6_7_2
   交易前置地址: tcp://121.37.80.177:20002
   初始化完成
  >>>>  交易前置连接成功
   [2024-07-21 16:43:56.975797]
  >>>>  客户端认证请求
   [2024-07-21 16:43:56.975797]
   发送请求: AppID=,AuthCode=,BrokerID=,UserID=4645,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: AppID=,AppType=,BrokerID=,UserID=4645,UserProductInfo=
  >>>>  用户登录请求
   [2024-07-21 16:43:56.975797]
   发送请求: BrokerID=,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=4645,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=成功
   响应内容: BrokerID=,CZCETime=16:43:57,DCETime=16:43:57,FFEXTime=16:43:57,FrontID=0,GFEXTime=,INETime=16:43:57,LoginTime=16:43:57,MaxOrderRef=1,SHFETime=16:43:57,SessionID=285880,SysVersion=,SystemName=Tick Trading System,TradingDay=20240721,UserID=4645
   ---
   交易日: 20240721
   交易系统名称: Tick Trading System
   后台版本信息:


   Enter any key to exit ...
  ```

## 行情API

- [x] 用户登录请求
- [x] 订阅行情

## 交易API

- [x] 客户端认证请求
- [x] 用户登录请求
- [x] 请求查询投资者
- [x] 请求查询投资者持仓
- [x] 请求查询投资者持仓明细
- [x] 请求查询报单
- [x] 请求查询成交
- [x] 请求查询资金账户
- [x] 请求查询合约
- [x] 请求查询产品
- [x] 请求查询合约手续费率
- [x] 请求查询合约保证金率
- [x] 请求查询报单手续费
- [x] 请求查询交易所
- [x] 报单录入请求
- [x] 报单撤销请求
- [x] 请求查询行情
- [x] 用户口令更新请求

## 其他

- [ ] k线合成