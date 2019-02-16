from django.shortcuts import render
from . import models


# Create your views here.
def index(request):
    post_list = models.Post.objects.all().order_by('created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
