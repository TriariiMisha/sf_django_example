from django.urls import include, path

urlpatterns = [
    path('', include('crm.internal.urls')),
    path('api/', include('crm.internal.swagger.urls')),
]
