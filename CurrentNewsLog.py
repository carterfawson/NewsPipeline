##This is the class that will keep a current account of what I have already sent to my news archive so that I am not sending any duplicates.
##For now I am just going to have it keep everything in memory, If I do the most recent API pulls then it should be okay
##If I get to the point though where I am still seeing duplicates then I can turn this into where the connection to the
#cloud archive is and we can check each article before sending it off.

##Also make sure that this dumps out whatever is in memory before the program exits if an exception is thrown or it is killed

class CurrentNewsLog:
    def __init__(self):
        self.log = {}

    def ReplaceSourceArticles(self, articles):
        self.log[articles['source']] = articles['articles']

    def CheckArticleDuplicate(self, article):
        if article['source_id'] in self.log:
            for old_article in self.log[article['source_id']]:
                if article['url'] == old_article['url']:
                    return True
        return False