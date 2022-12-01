from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.



def index(request):

    newsapi=NewsApiClient(api_key ='7e5c4b9eb7d24a2496b20d4495ce6a6a')
    top=newsapi.get_top_headlines(sources = 'techcrunch')

    I=top['articles']
    desc =[]
    news =[]
    img =[]


    for i in range(len(I)):
        f = I[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context ={"mylist":mylist})
