from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # urls handling api routing
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),
         name='user-detail'),
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(),
         name='customer-detail'),
    path('accounts/', views.AccountList.as_view(), name='account-list'),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name='account-detail'),
    path('transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(),
         name='transaction-detail'),
    path('atms/', views.ATMList.as_view(), name='atm-list'),
    path('atms/<int:pk>/', views.ATMDetail.as_view(), name='atm-detail'),
    path('atm-transactions/', views.ATMTransactionList.as_view(),
         name='atm-transaction-list'),
    path('atm-transactions/<int:pk>/',
         views.ATMTransactionDetail.as_view(), name='atm-transaction-detail'),


    # others
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
