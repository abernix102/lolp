from django.shortcuts import render
from django.views.generic import View 
# Create your views here.
from .forms import Post_Create_Forms

class Blog_list_view(View):
    def get(self, request, *args, **kwargs):
        context ={}
        return render(request, 'Blog_list.html', context)

class Blog_create_view(View):
    def get(self, request, *arg, **kwargs):
        context ={}
        return render(request, 'blog_create.html', context)
    def post(self, request, *arg, **kwargs):
        context={}
        return render(request, 'blog_create.html', context)