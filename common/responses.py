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


class BadInputError(APIException):
    """Readers error class"""
    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = HTTP_400_BAD_REQUEST
        self.detail = {"status": "failure", 'status_code': 400, 'message': msg, "data": []}

    def __str__(self):
        return str(self.detail)
