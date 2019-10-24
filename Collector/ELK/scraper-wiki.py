import sys
import json
import wikipedia

article_name = sys.argv[1]

try:
    wikipedia.set_lang("fr")
    list_articles = wikipedia.search(article_name)

    for article in list_articles:
        page = wikipedia.page(article)
        if "Catégorie:Portail:Entreprises/Articles liés" in page.categories:
            break

    article_dict = {"url" : page.url, "title" : page.title, 
            "description" : page.summary, "text" : page.content}

    print(json.dumps(article_dict), file=sys.stdout)
except Exception as e:
    print(str(e), file=sys.stderr)