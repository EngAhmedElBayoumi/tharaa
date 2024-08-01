from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('get_dev_sales_manager/<str:dev_sale>/', views.get_dev_sales_manager, name='get_dev_sales_manager'),
    path('get_broker_company_details/<str:company_name>/', views.get_broker_company_details, name='get_broker_company_details'),
    path('get_dev_sales_manager_details/<str:dev_sales_manager>/', views.get_dev_sales_manager_details, name='get_dev_sales_manager_details'),
    path('get_all_dev_sales_manager/', views.get_all_dev_sales_manager, name='get_all_dev_sales_manager'),
    #path('upload_data_from_csv/', views.upload_data_from_csv, name='upload_data_from_csv'),
]
