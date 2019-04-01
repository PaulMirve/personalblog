from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('article/', views.ArticleView.as_view(), name="article"),
    path('newpost/', views.CreatPostView.as_view(), name="new_post")
]