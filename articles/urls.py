from django.urls import path

from .views import ArticlesIndexView, ArticlesDetailView

urlpatterns = [
    path('investing/<int:year>/<int:month>/<int:day>/<str:slug>', ArticlesDetailView.as_view(), name='article'),
    path('', ArticlesIndexView.as_view(), name='home')
]