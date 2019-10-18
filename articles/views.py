from django.views.generic import TemplateView

from .services import ArticlesService

class ArticlesIndexView(TemplateView):
    template_name = 'articles_index.html'
    
    def featured(self):
        return ArticlesService().process('10-promise')['featured']
        
    def others(self):
        return ArticlesService().process('10-promise')['others']        