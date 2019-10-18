import json

class ArticlesService:
    articles = []
        
    def process(self, slug):
        with open('fixtures/content_api.json') as json_file:
            data = json.load(json_file)
            self.articles = data['results']
            return self.find_featured_article(slug)
            
            # for result in data['results']:
            #     print("oh hi there, friend")
                
    def find_featured_article(self, slug):
        featuredIndex = None
        for index in range(len(self.articles)):
            if self.articles[index]['uuid'] == 'a7acd8c8-c5ce-11e7-9fa6-0050569d4be0':
                featuredIndex = index
        
        featuredArticle = self.articles.pop(featuredIndex)
        return { 'featured': featuredArticle, 'others': self.articles }