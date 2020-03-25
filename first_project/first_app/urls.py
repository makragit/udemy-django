from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    path('form/', views.form, name='form'),

    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),

    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]