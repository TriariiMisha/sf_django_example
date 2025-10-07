from django.urls import path

from crm.core.views import alive

urlpatterns = [
    path('alive', alive, name='alive'),
]
