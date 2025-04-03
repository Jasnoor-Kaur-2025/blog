from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.blogIndex, name='blogIndex'),
    path('dashboard/', views.adminDashboard, name='adminDashboard'),
    path('add/', views.addBlog, name='addBlog'),
    path('edit/<int:id>/', views.editBlog, name='editBlog'),
    path('delete/<int:id>/', views.deleteBlog, name='deleteBlog'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #blogpage
    path('blog/<int:id>/', views.blog, name='blog'),
]
