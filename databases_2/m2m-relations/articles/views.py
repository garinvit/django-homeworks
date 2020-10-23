from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Relationship


def articles_list(request):
    template = 'articles/news.html'


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    context = {'object_list': Article.objects.all().order_by(ordering)}
    return render(request, template, context)
