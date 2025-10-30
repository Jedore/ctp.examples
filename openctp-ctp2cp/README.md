# openctp-ctp examples

## 快速上手

### 说明

提供了 以下 行情API 和 交易API 的多个接口代码示例。

`config.py` 是配置文件

`base_mdapi.py` 是行情API基类文件，可指定行情前置地址, 包了连接、登录 等基本逻辑

`base_tdapi.py` 是交易API基类文件，可指定交易前置地址, 包了连接、认证、登录 等基本逻辑

其他 `py` 文件均包含了一个具体的业务接口

除了 `config.py`, 其他 `py` 文件均可直接运行

> 注意：示例中的逻辑以 simnow 测试为准。在其他柜台可能逻辑有差异，比如过滤条件，在simnow无效，在其他柜台可能有效。

### 使用

- 准备 Python 环境 (3.7 ~ 3.14)
- 安装 [openctp-ctp](https://github.com/openctp/openctp-ctp-python)
- 克隆仓库
    ```bash
    git clone https://github.com/Jedore/ctp.examples.git
    cd ctp.examples/openctp-ctp
    ```
- 按需修改配置

  config.py

- 指定环境

  base_mdapi.py / base_tdapi.py

- 运行示例
  ```bash
  $ python base_tdapi.py
  >>>>  启动交易Api
   [2024-07-21 00:26:36.108030]
   投资者: 226485
   API版本: v6.7.2_20230913 10:48:10.4926
   交易前置地址: tcp://180.168.146.187:10130
   初始化完成
  >>>>  交易前置连接成功
   [2024-07-21 00:26:36.258365]
  >>>>  客户端认证请求
   [2024-07-21 00:26:36.258365]
   发送请求: AppID=simnow_client_test,AuthCode=0000000000000000,BrokerID=9999,UserID=226485,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=正确
   响应内容: AppID=simnow_client_test,AppType=1,BrokerID=9999,UserID=226485,UserProductInfo=
  >>>>  用户登录请求
   [2024-07-21 00:26:36.337245]
   发送请求: BrokerID=9999,ClientIPAddress=,ClientIPPort=0,InterfaceProductInfo=,LoginRemark=,MacAddress=,ProtocolInfo=,TradingDay=,UserID=226485,UserProductInfo=
   响应成功: ErrorID=0, ErrorMsg=正确
   响应内容: BrokerID=9999,CZCETime=00:26:36,DCETime=00:26:36,FFEXTime=00:26:36,FrontID=1,GFEXTime=00:26:36,INETime=00:26:36,LoginTime=00:26:39,MaxOrderRef=1,SHFETime=00:26:36,SessionID=-448170154,SysVersion=v6.7.3_20231222 14:00:35.6012.tkernel,SystemName=TradingHosting,TradingDay=20240719,UserID=226485
   ---
   交易日: 20240719
   交易系统名称: TradingHosting
   后台版本信息: v6.7.3_20231222 14:00:35.6012.tkernel
  ```

## 行情API

- [x] 用户登录请求
- [x] 订阅行情

## 交易API

- [x] 客户端认证请求
- [x] 用户登录请求
- [x] 请求查询投资者结算结果
- [x] 请求查询结算信息确认
- [x] 请求查询投资者
- [x] 请求查询投资者持仓
- [x] 请求查询投资者持仓明细
- [x] 请求查询报单
- [x] 请求查询成交
- [x] 请求查询资金账户
- [x] 请求查询合约
- [x] 请求查询产品
- [x] 请求查询交易编码
- [x] 请求查询合约手续费率
- [x] 请求查询合约保证金率
- [x] 请求查询报单手续费
- [x] 请求查询交易所
- [x] 请求查询签约银行
- [x] 报单录入请求
- [x] 报单撤销请求
- [x] 请求查询行情
- [x] 用户口令更新请求
- [x] 期货发起银行资金转期货请求
- [x] 期货发起期货资金转银行请求
- [x] 请求查询经纪公司交易参数
- [x] 请求查询银期签约关系

## 其他

- [ ] k线合成