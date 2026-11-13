from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from .models import Post, Comment
from .forms import CommentForm

@cache_page(300)
def posts_view(request):
    posts = Post.objects.all()
    print(posts)
    return render(request=request, template_name="posts.html", context={"posts": posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    
    return render(request, "post_detailed.html", {"post": post, "comments": comments})

def add_comment_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'post': post, 'form': form})