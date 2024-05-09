from django.urls import path
from .views import Blog_list_view, Blog_create_view, BlogDetailView
app_name = 'blog'

urlpatterns = [
    path('', Blog_list_view.as_view(), name='home'),
    path('create/', Blog_create_view.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail')
]   