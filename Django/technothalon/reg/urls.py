from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('new/', views.post_new, name='post_new'),
	path('zeus.html/', views.zeus, name='zeus'),
	path('apollo.html', views.apollo, name='apollo'),
	path('nike.html', views.nike, name='nike'),
	path('hermes.html', views.hermes, name='hermes'),
]