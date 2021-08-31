from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='start'),
    path('/thank-you-for-request', views.index),
]