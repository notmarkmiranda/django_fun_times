from django.urls import path

from .views import ArticlesIndexView

urlpatterns = [
    path('', ArticlesIndexView.as_view(), name='home')
]