import json
import random

class ArticlesService:
    articles = []
        
    def __init__(self):
        with open('fixtures/content_api.json') as json_file:
            data = json.load(json_file)
            self.articles = data['results']
            
    def find_featured_article(self, slug):
        featuredIndex = None
        for index in range(len(self.articles)):
            self.articles[index]['path'] = self.articles[index]['path'][:-5]
            if self.articles[index]['uuid'] == 'a7acd8c8-c5ce-11e7-9fa6-0050569d4be0':
                featuredIndex = index
        featuredArticle = self.articles.pop(featuredIndex)
        return { 'featured': featuredArticle, 'others': random.sample(self.articles, 3) }
    
    def find_article(self, path):
        article = None
        for index in range(len(self.articles)):
            if path in self.articles[index]["path"]:
                article = self.articles[index]
                break
        return article