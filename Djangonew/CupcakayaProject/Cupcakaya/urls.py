from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='Cupcakaya-Home'),
    path('menu', views.Menu, name='Menu'),
    path('Cupcakes', views.Cupcakes, name='Cupcakes'),
    path('about', views.about, name='about'),
    path('Cakepops', views.Cakepops, name='Cakepops'),
    path('Cakes', views.Cakes, name='Cakes'),
    path('Cookies', views.Cookies, name='Cookies'),
    path('faq', views.faq, name='faq'),
    path('cart', views.cart, name='cart'),
    path('form', views.form, name='form'),
    
    
   

]
