from django.views.generic import TemplateView
from django.shortcuts import render

from .services import ArticlesService

class ArticlesIndexView(TemplateView):
    template_name = 'articles_index.html'
    
    def featured(self):
        return ArticlesService().find_featured_article('10-promise')['featured']
        
    def others(self):
        return ArticlesService().find_featured_article('10-promise')['others']        
        
class ArticlesDetailView(TemplateView):
    template_name = 'articles_detail.html'
    
    def get(self, request, year, month, day, slug):
        article = ArticlesService().find_article('%s/%s/%s/%s'%(year, month, day, slug))
        return render(request, 'articles_detail.html', { 'article': article })