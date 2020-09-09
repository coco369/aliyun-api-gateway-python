
阿里云网关API-Python包使用规范
-------------------------------------------------


::

    from aliyun.api.gateway.sdk import client
    from aliyun.api.gateway.sdk.http import request
    from aliyun.api.gateway.sdk.common import constant

    host = "http://xxxx"
    url = "/api/vrp/express/areas"

    cli = client.DefaultClient(app_key="key", app_secret="secret")

    req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)

    data = cli.execute(req_post)

    print(data)
