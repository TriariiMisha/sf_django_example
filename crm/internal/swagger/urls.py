from django.urls import path

from crm.internal.swagger.views import schema_view_ws1, schema_view_ws1_swagger

urlpatterns = [
    path('schema', schema_view_ws1, name='schema'),
    path('schema/swagger-ui', schema_view_ws1_swagger, name='swagger-ui'),
]
