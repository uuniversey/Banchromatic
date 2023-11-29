from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/<str:name>/', views.profile),
    path('profilechange/<str:name>/', views.profilechange),
    path('registered_deposit/<str:name>/', views.registered_deposit),
    path('registered_saving/<str:name>/', views.registered_saving),
    path('join_deposit/<str:username>/', views.join_deposit),
    path('delete_deposit/<str:username>/', views.delete_deposit),
    path('join_saving/<str:username>/', views.join_saving),
    path('delete_saving/<str:username>/', views.delete_saving),
]