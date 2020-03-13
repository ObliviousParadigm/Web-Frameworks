from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('new/', views.post_new, name='post_new'),
	path('dist1.html/', views.dist1, name='dist1'),
	path('dist2.html', views.dist2, name='dist2'),
	path('dist3.html', views.dist3, name='dist3'),
	path('dist4.html', views.dist4, name='dist4'),
]
