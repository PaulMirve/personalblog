from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('article/', views.ArticleView.as_view(), name="article"),
    path('newpost/', views.CreatPostView.as_view(), name="new_post"),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]