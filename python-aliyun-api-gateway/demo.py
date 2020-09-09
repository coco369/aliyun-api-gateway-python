# -*- coding: utf-8 -*-
from aliyun.api.gateway.sdk import client
from aliyun.api.gateway.sdk.http import request
from aliyun.api.gateway.sdk.common import constant

host = "http://api-zto.dml-express.com"
url = "/api/vrp/express/areas"

cli = client.DefaultClient(app_key="key", app_secret="secret")

req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)

print('------')
print(cli.execute(req_post))

