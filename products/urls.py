from django.urls import path
from . import views


urlpatterns = [
	path('',views.index),
	path('new',views.new),
	path('<slug:slug>/', views.comment_detail, name='comment_detail')



]
