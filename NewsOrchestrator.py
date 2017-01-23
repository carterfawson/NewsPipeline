#on start it will load in all the news source names into memory
import NewsAPIConnection
import NewsStreamer
from multiprocessing import Pool
import CurrentNewsLog
import time

endless = True

while endless:
    sources = NewsAPIConnection.retrieveNewsSources()

    # pool = Pool()
    # pool.map(NewsStreamer.SendArticleToStream, articles['articles'])

    currentNews = CurrentNewsLog.CurrentNewsLog()

    for source in sources:
        articles = NewsAPIConnection.retrieveRecentNews(source['id'])
        for article in articles['articles']:
            article['source_id'] = source['id']
            article['source_name'] = source['name']
            article['source_category'] = source['category']
            article['source_country'] = source['country']
            if not currentNews.CheckArticleDuplicate(article):
                NewsStreamer.SendArticleToStream(article)
        currentNews.ReplaceSourceArticles(articles)

    time.sleep(1800)