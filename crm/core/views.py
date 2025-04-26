from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from crm.utils.response import UTF8JsonResponse


def alive(request):
    return HttpResponse('ok')


class MyselfView(APIView):
    @extend_schema(
        request=None,
        tags=['Myself'],
    )
    def get(self, request):
        return UTF8JsonResponse([], safe=False)
