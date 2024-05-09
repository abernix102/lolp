from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View 
# Create your views here.
from .forms import Post_Create_Forms
from .models import Post

class Blog_list_view(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context ={
            'posts': posts
        }
        return render(request, 'Blog_list.html', context)

class Blog_create_view(View):
    def get(self, request, *arg, **kwargs):
        form=Post_Create_Forms()
        context ={
            'form': form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *arg, **kwargs):
        if request.method=="POST":
            form = Post_Create_Forms(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')
        context={
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *arg, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post':post
        }
        return render(request,'blog_detail.html', context)