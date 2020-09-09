# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "http://api-zto.dml-express.com"
url = "/api/vrp/express/areas"

cli = client.DefaultClient(app_key="203851337", app_secret="Z5KKtq9pq9n6NFHT5JuZninroshenxKW")

req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)

print('------')
print(cli.execute(req_post))

