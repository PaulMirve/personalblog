from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
class ArticleView(TemplateView):
    template_name = 'blog/article.html'


class CreatPostView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'post_list.html'
    form_class = PostForm
    model = Post

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blog:post_list')


    





