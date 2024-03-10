from django.urls import path
from . import views

urlpatterns = [
    path('', views.signinup, name='signinup'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('projecthomepage/', views.projecthomepage, name='projecthomepage'),
    path('userhomepage/', views.userhomepage, name='userhomepage'),
    path('Contact/', views.Contact, name='Contact'),
    path('About/', views.About, name='About'),
    path('userviewhotel',views.userviewhotel,name='userviewhotel'),
    path('userviewprofile',views.userviewprofile,name='userviewprofile'),
    path('useraddemail',views.useraddemail,name='useraddemail'),
    path('useraddfirstname',views.useraddfirstname,name='useraddfirstname'),
    path('useraddlastname',views.useraddlastname,name='useraddlastname'),
    path('search',views.search_view,name='search_view')


]

