from django.urls import path
from . import views
#this is url file for account
urlpatterns = [
    path('',views.signup,name='signup'),



]
