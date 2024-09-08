from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-created_at'

    # 기본적으로 post_list.html을 템플릿으로 인식하므로 파일을 rename해주었다.
    # template_name = 'blog/index.html'

# 제너릭 뷰 클래스인 ListView를 상속한 PostList class에서 역할을 대신한다.
# def index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blog/index.html', {
#         'posts': posts
#     })

class PostDetail(DetailView):
    model = Post

# 제너릭 뷰 클래스인 DetailView를 상속한 PostDetail class에서 역할을 대신한다.
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, f'blog/single_post_page.html', {
#         'post': post
#     })