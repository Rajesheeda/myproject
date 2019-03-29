from django.shortcuts import render

from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    #Reporter.objects.get(full_name__contains='mith')
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
