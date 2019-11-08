'''
Created on 2019. 11. 6.

@author: legaltech
'''
from django.urls import path


from .import views

urlpatterns = [
    path('accountlist', views.getaccountlist, name='getaccountlist'),
    path('accountreg', views.accountreg, name='accountreg'),
    path('executeaccountregist', views.executeAccountRegist, name='executeaccountregist'),
    path('accountdel', views.accountdel, name='accountdel'),
    path('accountupdate', views.accountupdate, name='accountupdate'),
]
