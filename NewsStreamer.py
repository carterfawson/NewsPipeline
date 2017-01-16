import requests
import NewsAPIConfig
import json

def SendArticleToStream(article):
    try:
        r = requests.post(NewsAPIConfig.NodeRedPost, data=json.dumps(article))
    except:
        try:
            r = requests.post(NewsAPIConfig.NodeRedPost, data=json.dumps(article))
        except:
            print("this article could not be sent:")
            print(article)
