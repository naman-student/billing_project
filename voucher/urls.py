# urls for voucher app
from django.urls import path
from . import views

urlpatterns = [
    path('create_voucher/', views.create_voucher, name='create_voucher'),
    path('home/', views.home, name='home')
]
