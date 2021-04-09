import requests

api_key = "TihZvjetncNfABjEGJlIJIijoEqJpGtI"
news = "APPLE"
def pull_news(query_string):
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query_string}&api-key={api_key}"
    r = requests.get(url).json()['response']['docs']
    if len(r) > 0:
        return r
    return f"No existe noticias relacionas a {news}"
#print(pull_news(news))

def get_news(query_string):
    news = pull_news(query_string)
    news = [(n['abstract'], n['lead_paragraph'], n['pub_date']) for n in news]
    return news
print(get_news(news))