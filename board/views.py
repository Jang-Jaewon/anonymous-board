from django.shortcuts import render

def board(request):
    if request.method == 'GET':
        context = {
            'title': 'Hello',
        }
        return render(request, 'page/index.html', context=context)
