'''
Created on 2019. 11. 6.

@author: legaltech
'''
from django.urls import path
from .import views

urlpatterns = [
    path('accountlist', views.accountlist, name='accountlist'),
    path('accountreg', views.accountreg, name='accountreg'),
    path('executeaccountregist', views.executeAccountRegist, name='executeaccountregist'),
]
