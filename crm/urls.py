from django.urls import include, path

urlpatterns = [
    path('', include('crm.internal.urls')),
]
