from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def index(request):
    post_list = models.Post.objects.all().order_by('created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    # 用就是当传入的 pk 对应的 Post 在数据库存在时，
    # 就返回对应的 post，如果不存在，就给用户返回一个 404 错误，
    # 表明用户请求的文章不存在
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
