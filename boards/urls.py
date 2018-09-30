from django.urls import path
from . import views
# this file contain url for boards
urlpatterns = [
    path('boards/<int:pk>/',views.board_topics,name='board_topics'),
    path('boards/<int:pk>/new/',views.new_topic,name='new_topic'),
    #path('',views.home,name='home'),



]
