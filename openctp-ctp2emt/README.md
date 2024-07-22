# openctp-ctp2emt examples

使用 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 连接
 [东方财富EMT](https://github.com/openctp/openctp/tree/master/ctp2EMT)

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
- 安装 [openctp-ctp](https://github.com/openctp/openctp-ctp-python)  [openctp-ctp-channels](https://github.com/Jedore/openctp-ctp-channels)

  ```bash
  pip install openctp-ctp==6.6.7.*
  pip install openctp-ctp-channels
  ```

- 克隆仓库
    ```bash
    git clone https://github.com/Jedore/ctp.examples.git
    cd ctp.examples/openctp-ctp2emt
    ```
- 修改配置、用户名/密码

  config.py

- 指定环境

  base_mdapi.py / base_tdapi.py

- 将 openctp-ctp 切换为 emt 通道

  ```bash 
  openctp-channels switch emt
  ``` 
- 运行示例
  ```bash
  $ python base_tdapi.py
  >>>>  启动交易Api
   [2024-07-22 17:43:06.070789]
   投资者: 510100005510
   API版本: openctp-emt v6.3.19_P1
   交易前置地址: tcp://61.152.230.41:19088
   初始化完成
  >>>>  交易前置连接成功
   [2024-07-22 17:43:06.071788]
  >>>>  客户端认证请求
   [2024-07-22 17:43:06.071788]
   发送请求: AppID=1,AuthCode=,BrokerID=,UserID=510100005510,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: AppID=,AppType=,BrokerID=,UserID=510100005510,UserProductInfo=
  >>>>  用户登录请求
   [2024-07-22 17:43:06.071788]
   发送请求: BrokerID=,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=510100005510,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: BrokerID=,CZCETime=17:43:06,DCETime=17:43:06,FFEXTime=17:43:06,FrontID=0,INETime=17:43:06,LoginTime=17:43:06,MaxOrderRef=1,SHFETime=17:43:06,SessionID=1,SystemName=EMT,TradingDay=20240722,UserID=510100005510
   ---
   交易日: 20240722
   交易系统名称: EMT
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