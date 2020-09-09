
### 介绍API网关

##### 1、API网关（API Gateway），提供API托管服务，覆盖设计、开发、测试、发布、售卖、运维监测、安全管控、下线等API各个生命周期阶段，帮助您快速建设以API为核心的系统架构。

### Demo说明

##### 1、本示例的 Python 版本为3.7.6
##### 2、本demo主要是为了提供签名方法，调用示例可以参考 Demo.py 文件
##### 3、使用注意事项：
   
   - [签名文档](https://help.aliyun.com/document_detail/29475.html?spm=a2c4g.11186623.6.582.4a097ad1F4m0QE)

### pip安装

```
pip install python-aliyun-api-gateway
```

### 使用

```
# -*- coding: utf-8 -*-
from aliyun.api.gateway.sdk import client
from aliyun.api.gateway.sdk.http import request
from aliyun.api.gateway.sdk.common import constant

host = "http://xxxx"
url = "/api/vrp/express/areas"

cli = client.DefaultClient(app_key="key", app_secret="secret")

req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)

data = cli.execute(req_post)

print(data)

```