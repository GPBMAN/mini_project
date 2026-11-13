from django.urls import path
from .views import * 

urlpatterns = [
    path("posts/", posts_view, name="all_posts"),
    path("post/<int:pk>/", post_detail_view, name="post_detail"),
    path("post/<int:pk>/comment/", add_comment_view, name="add_comment"),
]