from crm.internal.swagger.views import schema_view_ws1, schema_view_ws1_swagger
from django.urls import path

urlpatterns = [
    path('api/schema/', schema_view_ws1, name='schema'),
    path('api/schema/swagger-ui/', schema_view_ws1_swagger, name='swagger-ui'),
]
