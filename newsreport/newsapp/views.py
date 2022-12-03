from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.



def index(request):

    newsapi=NewsApiClient(api_key ='your api key enter here')
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
