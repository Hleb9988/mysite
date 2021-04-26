from django.http import HttpResponse
from django.shortcuts import render

from .models import News

def index(requests):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }

    return render(requests, template_name='news/index.html',context=context)
