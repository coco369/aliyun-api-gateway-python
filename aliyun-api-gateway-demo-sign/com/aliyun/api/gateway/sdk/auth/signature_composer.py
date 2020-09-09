from com.aliyun.api.gateway.sdk.common import constant


def build_sign_str(uri=None, method=None, headers=None, body=None):
    lf = '\n'
    string_to_sign = []
    string_to_sign.append(method)

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_ACCEPT in headers and headers[constant.HTTP_HEADER_ACCEPT]:
        string_to_sign.append(headers[constant.HTTP_HEADER_ACCEPT])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_CONTENT_MD5 in headers and headers[constant.HTTP_HEADER_CONTENT_MD5]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_MD5])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_CONTENT_TYPE in headers and headers[constant.HTTP_HEADER_CONTENT_TYPE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_CONTENT_TYPE])

    string_to_sign.append(lf)
    if constant.HTTP_HEADER_DATE in headers and headers[constant.HTTP_HEADER_DATE]:
        string_to_sign.append(headers[constant.HTTP_HEADER_DATE])

    string_to_sign.append(lf)
    string_to_sign.append(_format_header(headers=headers))
    string_to_sign.append(_build_resource(uri=uri, body=body))

    return ''.join(string_to_sign)


def _build_resource(uri="", body={}):
    if uri.__contains__("?"):
        uri_array = uri.split("?")
        uri = uri_array[0]
        query_str = uri_array[1]
        if not body:
            body = {}
        if query_str:
            query_str_array = query_str.split("&")
            for query in query_str_array:
                query_array = query.split("=")
                if query_array[0] not in body:
                    body[query_array[0]] = query_array[1]

    resource = []
    resource.append(uri)
    if body:
        resource.append("?")
        param_list = body.keys()
        param_list = sorted(param_list)
        first = True
        for key in param_list:
            if not first:
                resource.append("&")
            first = False

            if body[key]:
                resource.append(key)
                resource.append("=")
                resource.append(body[key])
            else:
                resource.append(key)

    if resource is None:
        return ''

    return "".join(str(x) for x in resource)


def convert_utf8(input_string):
    # if isinstance(input_string, unicode):
    #     input_string = input_string.encode('utf-8')
    input_string = input_string.encode('utf-8')
    return input_string


def _format_header(headers={}):
    """
    :param headers: 请求头
    以{HeaderName}:{HeaderValue} + "\n"的方式按照字符串顺序从小到大顺序添加, 建议加入签名的头为X-Ca-Key,X-Ca-Nonce, 其他头客户端实现可自行选择是否加入签名。
    """
    lf = '\n'
    temp_headers = []
    if len(headers) > 0:
        header_list = headers.keys()
        header_list = sorted(header_list)
        signature_headers = []
        for k in header_list:
            if k.startswith("X-Ca-"):
                temp_headers.append(k)
                temp_headers.append(":")
                temp_headers.append(str(headers[k]))
                temp_headers.append(lf)
                signature_headers.append(k)
        headers[constant.X_CA_SIGNATURE_HEADERS] = ','.join(signature_headers)
    return ''.join(temp_headers)
