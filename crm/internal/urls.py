from django.urls import include, path

urlpatterns = [
    path('api/', include('crm.core.urls')),
    path('', include('crm.internal.swagger.urls')),
]
