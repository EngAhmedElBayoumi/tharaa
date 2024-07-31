from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('get_dev_sales_manager/<str:dev_sale>/', views.get_dev_sales_manager, name='get_dev_sales_manager'),
]
