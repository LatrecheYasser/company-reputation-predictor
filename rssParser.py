import feedparser
from newspaper import Article

fileOut = open("logStash.conf", 'w')
fileOut.writelines("input {\n")

with open("rssLinks.txt", "r") as fileIn:
    for line in fileIn:
        if "http" in line:
            try:
                feed = feedparser.parse(line)
                post = feed.entries[0]
                article = Article(url=post.link, language="fr")
                article.download()
                article.parse()
                fileOut.writelines("\n".join(('	rss {', '		interval => 3600', '		url => "' + line[:-1] + '"', '	}\n')))
            except Exception as e:
                print(line+" : "+str(e))

fileOut.writelines("}\n")

with open("Template.conf", "r") as fileIn:
    fileOut.writelines(fileIn.readlines())
fileOut.close()
