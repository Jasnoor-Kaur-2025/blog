from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import BlogPost
from .forms import BlogPostForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

def blogIndex(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blogIndex.html', {'blogs':blogs})

def blog(request, id):
    blog = get_object_or_404(BlogPost, id = id)
    return render(request, 'blog.html', {'blog':blog})

@login_required(login_url='/login/')
@user_passes_test(is_admin, login_url='/login/')
def adminDashboard(request):
    blogs = BlogPost.objects.all()
    return render(request, 'admin_Dashboard.html', {'blogs':blogs})

@login_required(login_url='/login/')
@user_passes_test(is_admin, login_url='/login/')
def addBlog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('adminDashboard')
        
    else:
        form = BlogPostForm()
    
    return render(request, 'add_blog.html', {'form':form})

@login_required(login_url='/login/')
@user_passes_test(is_admin, login_url='/login/')
def editBlog(request, id):
    blog = get_object_or_404(BlogPost, id = id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('adminDashboard')
    else:
        form = BlogPostForm(instance=blog)
    
    return render(request, 'edit_blog.html', {'form':form})

@login_required(login_url='/login/')
@user_passes_test(is_admin, login_url='/login/')
def deleteBlog(request, id):
    blog = get_object_or_404(BlogPost, id = id)
    blog.delete()
    return redirect('adminDashboard')
