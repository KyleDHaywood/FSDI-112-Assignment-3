from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post


# API view for Post
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     http_method_names = [ "get", "post", "patch", "put", "delete" ]



# Create your views here.


class PostListView(ListView):
    template_name = "posts/posts_list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'theme', 'author', 'text']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title','theme', 'text']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

