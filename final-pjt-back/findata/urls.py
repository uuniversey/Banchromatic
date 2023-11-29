
from django.urls import path
from . import views

app_name = 'findata'
urlpatterns = [
    path('deposit/', views.save_data_deposit),
    path('saving/', views.save_data_saving),
    path('showdepositproducts/', views.show_deposit_products),
    path('showdepositoptions/', views.show_deposit_options),
    path('showsavingproducts/', views.show_saving_products),
    path('showsavingoptions/', views.show_saving_options),
    path('exchangerates/', views.exchangerates),
    path('showexchangerates/', views.showexchangerates),
    path('detail_d/<str:name>/', views.detail_deposit),
    path('detail_s/<str:name>/', views.detail_savings),
    path('exchange_calc/<str:name1>/<str:name2>/', views.exchange_calc),
]