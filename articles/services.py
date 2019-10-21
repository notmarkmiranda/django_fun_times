import json
import random
from django.utils.dateparse import parse_datetime

class ArticlesService:
    articles = []
        
    def __init__(self):
        with open('fixtures/content_api.json') as json_file:
            data = json.load(json_file)
            self.articles = data['results']
            for article in self.articles:
                article['path'] = article['path'][:-5] 
                article['publish_at_with_time'] = parse_datetime(article['publish_at']).strftime('%B %-e, %Y at %I:%M%p')
                article['publish_at'] = parse_datetime(article['publish_at']).strftime('%B %-e, %Y')
                article['body'] = article['body'].replace('<p>{%sfr%}</p>', '')
            
    def find_featured_article(self, slug):
        featuredIndex = None
        for index in range(len(self.articles)):
            for tag in self.articles[index]['tags']:
                if tag['slug'] == slug:
                    featuredIndex = index
                    break
            if featuredIndex is not None:
                break
        featuredArticle = self.articles.pop(featuredIndex)
        return { 'featured': featuredArticle, 'others': random.sample(self.articles, 3) }
    
    def find_article_by_path(self, path):
        article = None
        for index in range(len(self.articles)):
            if path in self.articles[index]["path"]:
                article = self.articles[index]
                break
        return article
        
class QuotesService:
    quotes = []
    
    def __init__(self):
        with open('fixtures/quotes_api.json') as json_file:
            data = json.load(json_file)
            for quote in data:
                new_quote = {
                    'name': quote['CompanyName'],
                    'market': quote['ExchangeName'],
                    'symbol': quote['Symbol'],
                    'image': 'https://g.foolcdn.com/art/companylogos/mark/%s.png' % (quote['Symbol']),
                    'currentPrice': quote['CurrentPrice']['Amount'],
                    'change': quote['Change']['Amount'],
                    'percentChange': self.format_percentage(quote['PercentChange']['Value']),
                    'positive': True if quote['Change']['Amount'] > 0.0 else False
                }
                self.quotes.append(new_quote)
    
    def all_quotes(self):
        return self.quotes
        
    def format_percentage(self, number):
        percentage = float(int(number * 10000)) / 100
        if number < 0:
            return f'({percentage}%)'
        else:
            return f'{percentage}%'