import sys
from newspaper import Article

url = sys.argv[1]
article = Article(url=url, language="fr")
article.download()
try:
    article.parse()
    print(article.text, file=sys.stdout)
except Exception as e:
    print(str(e) , file=sys.stderr)