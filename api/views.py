from django.http import HttpResponse


def get_rec(request):
    return HttpResponse('get ruchka')


def add_rec(request):
    return HttpResponse('post ruchka')


def moon_news(request):
    return HttpResponse('World news ruchka')
