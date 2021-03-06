from django.urls import path
from .views import  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view() , name='home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new_post/', PostCreateView.as_view(), name='postnew'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='postupdate'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='postdelete'),
]
