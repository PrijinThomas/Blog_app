from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('admin-dashboard/users/', views.admin_user_list_view, name='admin_user_list'),
    path('admin-dashboard/posts/', views.admin_post_list_view, name='admin_post_list'),
    path('admin-dashboard/posts/<int:pk>/delete/', views.admin_post_delete_view, name='admin_post_delete'),
]
