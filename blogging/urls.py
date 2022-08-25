from django.urls import path, include
from blogging.views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="post_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
]
