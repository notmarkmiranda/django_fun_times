from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse

import json

from .services import ArticlesService, QuotesService
from .models import Comment
from .forms import CommentForm

class ArticlesIndexView(TemplateView):
    def get(self, request):
        all_articles = ArticlesService().find_featured_article('10-promise')
        return render(request, 'articles_index.html', { 'featured': all_articles['featured'], 'articles': all_articles['others'], 'detail': False })
    
class ArticlesDetailView(CreateView):
    def get(self, request, year, month, day, slug):
        article = ArticlesService().find_article_by_path('%s/%s/%s/%s' % (year, month, day, slug))
        comments = Comment.objects.filter(article_uuid=article['uuid']).order_by('created_at')
        form = CommentForm()
        return render(request, 'articles_detail.html', { 'article': article, 'comments': comments, 'form': form })
    
    def post(self, request, year, month, day, slug):
        form = CommentForm(request.POST)
        article = ArticlesService().find_article_by_path('%s/%s/%s/%s' % (year, month, day, slug))
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_uuid = article['uuid']
            comment.save()
            return redirect(reverse('article', kwargs={ 'year': year, 'month': month, 'day': day, 'slug': slug }))
        return render(request, 'articles_detail.html', { 'article': article })