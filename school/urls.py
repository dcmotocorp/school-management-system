"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from.models import *
urlpatterns = [
    path('index/',views.add,name='add'),
    path('about/',views.add1,name='add1'),
    path('codes/',views.add2,name='add2'),
    path('contact/',views.add3,name='add3'),
    path('gallery/',views.add4,name='add4'),
    path('services/',views.add5,name='add5'),
    path('r-student/',views.add6,name='add6'),
    path('f-student/', views.add7, name='add7'),
    path('login-student/',views.add8,name='add8'),
    path('register/',views.registration,name='registration'),
    path('loginredirect/',views.loginredirect,name='loginredirect'),
    path('logout/', views.logout, name='logout'),
    path('view-all/', views.view_all, name='view-all'),
    path('delete-data/<int:pk>', views.delete_data, name='delete-data'),
    path('edit-data/<int:ck>', views.edit_data, name='edit-data'),
    path('edit-page/', views.edit_page, name='edit-page'),
path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
path('sentotp/', views.sentotp, name='sentotp'),
path('reset/', views.reset, name='reset'),


]
