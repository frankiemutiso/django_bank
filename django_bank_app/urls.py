from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('transfer/', views.transfer, name='transfer'),
    path('transfer_process/', views.transfer_process, name='transfer_process'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdraw_process/', views.withdraw_process, name='withdraw_process'),
    path('atm_withdrawal/', views.atm_withdrawal, name='atm_withdrawal'),
    path('atm_withdrawal_process/', views.atm_withdrawal_process,
         name='atm_withdrawal_process'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout')
]
