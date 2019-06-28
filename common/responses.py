from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST


def data_response(code, data, status="success", message=None):
    if message:
        return Response({
            'status_code': code,
            'status': status,
            'data': data,
            'message': message
        }, status=code)
    else:
        return Response({
            'status_code': code,
            'status': status,
            'data': data
        }, status=code)


class BaseError(APIException):
    def __init__(self, msg, status_code):
        APIException.__init__(self, msg)
        self.status_code = status_code
        self.detail = {"status": "failure", 'status_code': status_code, 'message': msg, "data": []}


class BadInputError(BaseError):
    def __init__(self, msg):
        super().__init__(msg, 400)


class ServerError(APIException):
    def __init__(self, msg):
        super().__init__(msg, 500)
