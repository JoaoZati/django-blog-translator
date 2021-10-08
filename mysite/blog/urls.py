from . import views
from django.urls import path


urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('posts/', views.PostList.as_view(), name='posts_view'),
]
