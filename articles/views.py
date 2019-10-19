from django.views.generic import TemplateView
from django.shortcuts import render

from .services import ArticlesService

class ArticlesIndexView(TemplateView):
    def get(self, request):
        all_articles = ArticlesService().find_featured_article('10-promise')
        return render(request, 'articles_index.html', { 'featured': all_articles['featured'], 'articles': all_articles['others'], 'detail': False })
    
class ArticlesDetailView(TemplateView):
    def get(self, request, year, month, day, slug):
        article = ArticlesService().find_article_by_path('%s/%s/%s/%s' % (year, month, day, slug))
        return render(request, 'articles_detail.html', { 'article': article, 'detail': True })