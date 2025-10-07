from django.urls import include, path

urlpatterns = [
    path('api/', include('crm.core.urls')),
    path('api/', include('crm.internal.products.urls')),
]
