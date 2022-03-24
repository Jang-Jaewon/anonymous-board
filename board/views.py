from django.shortcuts import render
from django.core.paginator import Paginator

from board.models import Post


def board(request):
    if request.method == 'GET':
        page        = request.GET.get('page', 1)
        search_text = request.GET.get('search_text', "")
        post_set    = Post.objects.filter(title__icontains=search_text).order_by('-id')
        
        paginator = Paginator(post_set, 6)
        post_set  = paginator.get_page(page)
        
        context = {
            'post_set': post_set,
            'search_text': search_text,
        }
        return render(request, 'page/index.html', context=context)
