from django.urls import path

from crm.core.views import alive, MyselfView

urlpatterns = [
    path('alive/', alive, name='alive'),
    path('myself/', MyselfView.as_view()),
]