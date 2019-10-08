import sys
from newspaper import Article

url = sys.argv[1]

article = Article(url)
article.download()
if article.is_valid_url():
    article.parse()
    print(article.text)
else:
    print("Error downloading article: " + url, file=sys.stderr)