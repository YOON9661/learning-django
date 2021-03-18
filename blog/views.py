from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    # 역순으로 정렬 order_by('-pk')
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )
