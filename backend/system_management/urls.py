from django.urls import path

from system_management import views

urlpatterns = [

    # User authentication
    path('user_login/', views.user_login, name='user_login'),
    path('user_sign_up/', views.user_sign_up, name='user_sign_up'),
]