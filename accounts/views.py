from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from blog.models import BlogPost
from .forms import UserRegisterForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful! Welcome to BlogApp.")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

@login_required
def profile_view(request):
    user_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'accounts/profile.html', {
        'user_posts': user_posts
    })

@user_passes_test(lambda u: u.is_active and u.is_staff, login_url='login')
def admin_dashboard_view(request):
    total_users = User.objects.count()
    total_posts = BlogPost.objects.count()
    latest_users = User.objects.order_by('-date_joined')[:5]
    latest_posts = BlogPost.objects.order_by('-created_at')[:5]
    return render(request, 'accounts/admin_dashboard.html', {
        'total_users': total_users,
        'total_posts': total_posts,
        'latest_users': latest_users,
        'latest_posts': latest_posts,
    })

@user_passes_test(lambda u: u.is_active and u.is_staff, login_url='login')
def admin_user_list_view(request):
    users = User.objects.order_by('-date_joined')
    return render(request, 'accounts/user_list.html', {'users': users})

@user_passes_test(lambda u: u.is_active and u.is_staff, login_url='login')
def admin_post_list_view(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'accounts/admin_post_list.html', {'posts': posts})

@user_passes_test(lambda u: u.is_active and u.is_staff, login_url='login')
def admin_post_delete_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        title = post.title
        post.delete()
        messages.success(request, f"Post '{title}' deleted successfully by Administrator.")
        return redirect('admin_post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post, 'is_admin_delete': True})
