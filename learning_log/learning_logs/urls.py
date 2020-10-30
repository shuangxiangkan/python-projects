# Define URL patterns for learning_logs

from django.conf.urls import url
from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),

    # show all topics
    path('topics/', views.topics, name='topics'),

    # 特定主题的详细页面
    path("topics/(?P<topic_id>\d+)/", views.topic, name='topic'),
   ]
