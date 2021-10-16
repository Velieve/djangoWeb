from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'djWebs'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
]