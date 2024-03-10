from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotelhome, name='hotelhome'),
    path('uploadhotel/', views.uploadhotel, name='uploadhotel'),
    path('viewhotel/', views.viewhotel, name='viewhotel'),
    path('hotelviewprofile/', views.hotelviewprofile, name='hotelviewprofile'),
    path('hoteladdemail', views.hoteladdemail, name='hoteladdemail'),
    path('hoteladdfirstname', views.hoteladdfirstname, name='hoteladdfirstname'),
    path('hoteladdlastname', views.hoteladdlastname, name='hoteladdlastname'),
    path('hotelstaffmanagementht', views.hotelstaffmanagementht, name='hotelstaffmanagementht'),
    path('hoteladdstaff', views.hoteladdstaff, name='hoteladdstaff'),
    path('hotelremovestaff/<int:id>/', views.hotelremovestaff, name='hotelremovestaff'),
    path('hotelupdatestaff/<int:id>/', views.hotelupdatestaff, name='hotelupdatestaff'),


]
