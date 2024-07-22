# openctp-ctp2xtp examples

使用 [openctp-ctp](https://github.com/openctp/openctp-ctp-python) 连接
 [中泰证券XTP柜台](https://github.com/openctp/openctp/tree/master/ctp2XTP)

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
  pip install openctp-ctp==6.6.1.*
  pip install openctp-ctp-channels
  ```

- 克隆仓库
    ```bash
    git clone https://github.com/Jedore/ctp.examples.git
    cd ctp.examples/openctp-ctp2xtp
    ```
- 修改配置、用户名/密码、appid

  config.py

- 指定环境

  base_mdapi.py / base_tdapi.py

- 将 openctp-ctp 切换为 xtp 通道

  ```bash 
  openctp-channels switch xtp
  ``` 
- 运行示例
  ```bash
  $ python base_tdapi.py
  >>>>  启动交易Api
   [2024-07-22 17:52:38.881843]
   投资者: 253191003633
   API版本: V6_6_1_P1
   交易前置地址: tcp://122.112.139.0:6102
   初始化完成
  >>>>  交易前置连接成功
   [2024-07-22 17:52:38.882845]
  >>>>  客户端认证请求
   [2024-07-22 17:52:38.882845]
   发送请求: AppID=b8aa7173bba3470e390d787219b2112e,AuthCode=1,BrokerID=1080,UserID=253191003633,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: AppID=,AppType=,BrokerID=1080,UserID=253191003633,UserProductInfo=
  >>>>  用户登录请求
   [2024-07-22 17:52:38.898845]
   发送请求: BrokerID=1080,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=253191003633,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=
   响应内容: BrokerID=1080,CZCETime=17:52:39,DCETime=17:52:39,FFEXTime=17:52:39,FrontID=0,INETime=17:52:39,LoginTime=17:52:39,MaxOrderRef=1,SHFETime=17:52:39,SessionID=1,SystemName=XTP,TradingDay=20240722,UserID=253191003633
   ---
   交易日: 20240722
   交易系统名称: XTP
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