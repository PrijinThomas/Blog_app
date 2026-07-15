from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Create Blog Post'})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
        messages.error(request, "You can only edit your own blog posts.")
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'title': 'Edit Blog Post', 'post': post})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.author != request.user:
        messages.error(request, "You can only delete your own blog posts.")
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
