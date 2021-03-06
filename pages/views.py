from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from pages.models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'all_posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'pages/new_post.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'pages/post_update.html'
    fields = ['title', 'body']
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')