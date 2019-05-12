from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView,)
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comments
from blog.forms import PostForm, CommentsForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import JsonResponse

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


class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = CommentsForm
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments_form'] = CommentsForm()
        return context
    
    

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class CreateCommentsView(CreateView):
    form_class = CommentsForm
    model = Comments
    

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'blog/comments_form.html', {'form': form})

class CommentsDeleteView(DeleteView):
    model = Comments
    success_url = reverse_lazy('blog:post_list')

class CommentsUpdateView(UpdateView):
    redirect_field_name = 'blog/post_detail.html'
    form_class = CommentsForm
    model = Comments

def process_like(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(id=post_id)
    post.process_likes()
    return render(request, 'blog/post_list.html')


def print_hi(request, pk):
    print('Hi there!')
    post = get_object_or_404(Post, pk=pk)
    post.process_likes()
    post.save()
    return redirect('blog:post_detail', pk=post.pk)

def highlight_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.highlight_post()
    post.save()
    return  redirect('blog:post_list')

def remove_highlight(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.remove_highlight()
    post.save()
    return  redirect('blog:post_list')