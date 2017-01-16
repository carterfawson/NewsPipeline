import NewsAPIConfig
import requests

def retrieveNewsSources():
    r = requests.get("https://newsapi.org/v1/sources?language=en")
    return r.json()['sources']

def retrieveRecentNews(sourceName):
    r = requests.get("https://newsapi.org/v1/articles?source=%s&apiKey=%s" % (sourceName, NewsAPIConfig.APIkey))
    return r.json()