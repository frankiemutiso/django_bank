from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewset)
router.register(r'accounts', views.AccountViewset)
router.register(r'transactions', views.TransactionViewset)
router.register(r'atms', views.ATMViewset)
router.register(r'atm_transactions', views.ATMTransactionViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.registration, name="register")

]
