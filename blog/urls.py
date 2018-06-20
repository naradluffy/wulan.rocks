from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:project_id>/', views.detail, name='detail'),
	path('category/<int:category_id>/', views.category, name='category'),
	path('contact/', views.contact, name='contact'),
	path('about/',views.about, name='about'),
]
