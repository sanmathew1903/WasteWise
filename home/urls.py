from django.urls import path
from . import views
urlpatterns=[
    path('',views.signin,name='signin'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('index',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),


    path('order',views.order,name='order'),
]