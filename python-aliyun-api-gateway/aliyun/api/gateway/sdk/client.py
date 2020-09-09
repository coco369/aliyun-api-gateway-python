from aliyun.api.gateway.sdk.util import UUIDUtil, DateUtil
from aliyun.api.gateway.sdk import Response
from aliyun.api.gateway.sdk.common import constant
from aliyun.api.gateway.sdk.auth import sha_hmac256, signature_composer, md5_tool


class DefaultClient:
    def __init__(self, app_key=None, app_secret=None, time_out=None):
        self.__app_key = app_key
        self.__app_secret = app_secret
        self.__time_out = time_out

    def execute(self, request=None):
        try:
            headers = self.build_headers(request)
            print(headers)

            response = Response(host=request.get_host(), url=request.get_url(), method=request.get_method(),
                                headers=headers, protocol=request.get_protocol(), content_type=request.get_content_type(),
                                content=request.get_body(), time_out=request.get_time_out())
            if response.get_ssl_enable():
                return response.get_https_response()
            else:
                return response.get_http_response()
        except IOError:
            raise
        except AttributeError:
            raise

    def build_headers(self, request=None):
        headers = dict()
        header_params = request.get_headers()
        headers[constant.X_CA_TIMESTAMP] = DateUtil.get_timestamp()
        headers[constant.X_CA_KEY] = self.__app_key

        body = request.get_body()

        headers[constant.X_CA_NONCE] = UUIDUtil.get_uuid()

        if request.get_content_type():
            headers[constant.HTTP_HEADER_CONTENT_TYPE] = request.get_content_type()
        else:
            headers[constant.HTTP_HEADER_CONTENT_TYPE] = constant.CONTENT_TYPE_JSON

        if constant.HTTP_HEADER_ACCEPT in header_params \
                and header_params[constant.HTTP_HEADER_ACCEPT]:
            headers[constant.HTTP_HEADER_ACCEPT] = header_params[constant.HTTP_HEADER_ACCEPT]
        else:
            headers[constant.HTTP_HEADER_ACCEPT] = constant.CONTENT_TYPE_JSON

        if constant.POST == request.get_method() and constant.CONTENT_TYPE_STREAM == request.get_content_type():
            headers[constant.HTTP_HEADER_CONTENT_MD5] = md5_tool.get_md5_base64_str(request.get_body())
            str_to_sign = signature_composer.build_sign_str(uri=request.get_url(), method=request.get_method(),
                                                            headers=headers)
        else:
            str_to_sign = signature_composer.build_sign_str(uri=request.get_url(), method=request.get_method(),
                                                            headers=headers, body=body)
            print(str_to_sign)

        headers[constant.X_CA_SIGNATURE] = sha_hmac256.sign(str_to_sign, self.__app_secret)
        return headers
