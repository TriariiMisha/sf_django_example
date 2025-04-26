from django.http.response import JsonResponse
from djangorestframework_camel_case.util import camelize


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {'ensure_ascii': False, **(json_dumps_params or {})}
        super().__init__(camelize(*args), json_dumps_params=json_dumps_params, **kwargs)
