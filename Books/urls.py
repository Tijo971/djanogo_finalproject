from django.urls import path
from Books import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('savecategory/', views.savecategory, name='savecategory'),
    path('categorylist/', views.categorylist, name='categorylist'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('categorydelete/<int:dataid>/', views.categorydelete, name='categorydelete'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logindatas/', views.logindatas, name='logindatas'),
    path('logutpage/', views.logutpage, name='logutpage'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('savebook/', views.savebook, name='savebook'),
    path('booklist/', views.booklist, name='booklist'),
    path('editbook/<int:dataid>/', views.editbook, name='editbook'),
    path('updatebook/<int:dataid>/', views.updatebook, name='updatebook'),
    path('Bookdelete/<int:dataid>/', views.Bookdelete, name='Bookdelete'),
    path('upcommingbooks/', views.upcommingbooks, name='upcommingbooks'),
    path('saveupcomebk/', views.saveupcomebk, name='saveupcomebk'),
]