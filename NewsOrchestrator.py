#on start it will load in all the news source names into memory
import NewsAPIConnection
import NewsStreamer
from multiprocessing import Pool

sources = NewsAPIConnection.retrieveNewsSources()

pool = Pool()

for source in sources:
    articles = NewsAPIConnection.retrieveRecentNews(source['id'])
    pool.map(NewsStreamer.SendArticleToStream, articles['articles'])
