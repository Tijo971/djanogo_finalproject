from django.urls import path
from Webbooks import views


urlpatterns=[
    path('homepage/', views.homepage, name='homepage'),
    path('products/<cat_nme>', views.products, name='products'),
    path('singleproduct/<dataid>/', views.singleproduct, name='singleproduct'),
    path('reg_login/', views.reg_login, name='reg_login'),
    path('usersignin/', views.usersignin, name='usersignin'),
    path('loginprocess/', views.loginprocess, name='loginprocess'),
    path('logutpage/', views.logutpage, name='logutpage'),
    path('cart/', views.cart, name='cart'),
    path('savecart/', views.savecart, name='savecart'),
    path('cartdelete/<dataid>', views.cartdelete, name='cartdelete'),
    path('checkout/', views.checkout, name='checkout'),
    path('storecheckout/', views.storecheckout, name='storecheckout'),
]