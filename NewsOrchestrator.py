#on start it will load in all the news source names into memory
import NewsAPIConnection
import NewsStreamer
from multiprocessing import Pool

sources = NewsAPIConnection.retrieveNewsSources()

pool = Pool()
#pool.map(NewsStreamer.SendArticleToStream, articles['articles'])

for source in sources:
    articles = NewsAPIConnection.retrieveRecentNews(source['id'])
    #for article in articles['articles']:
        #NewsStreamer.SendArticleToStream(article)
    pool.map(NewsStreamer.SendArticleToStream, articles['articles'])
