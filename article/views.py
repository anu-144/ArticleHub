from django.shortcuts import render
from.models import Article

articles=[
        {"id":1,"article1":"Sports News🎾🏏🏓", "desc":"Champions trophy final Rohit Sharma and Shubman Gill - Thd Hitman-Iceman combo give India edge over opponents"},
        {"id":2,"article1": "Science News🧪🔬🌙🌓","desc":"Chandrayan-3 data hints at hidden water-ice beyond moon's polar regions"}, 
        {"id":3,"article1": "Political News🗞️📰","desc":"Immigration and Foreigners Bill, 2025 introduced in Lok Sabha"}, 
]
articles=Article.objects.all()
def home6(request):
    return render(request, 'pages/home6.html',{"data1":'this is the data sent from backend'})



def contact6(request):
    search = request.GET.get('search')
    result = []

    if search:
        for article in articles:
            if search.lower() in article.article1.lower():  
                result.append({"id": article.id, "article1": article.article1, "desc": ""})
            elif search.lower() in article.desc.lower():  
                result.append({"id": article.id, "article1": article.article1, "desc": article.desc})
    else:
        result = [{"id": article.id, "article1": article.article1, "desc": ""} for article in articles]

    context = {
        "data2": "happy to learn context",
        "data3": "this is context",
        'title': 'article',
        'articles': result,
    }
    return render(request, 'pages/contact6.html', context)



def about6(request):
    return render(request,'pages/about6.html')

def article(request,id):
    data=None
    for article in articles:
        if article.id==id:
            data=article
    context={
        'title':'article_page',
        'article':data
    }
    return render(request,'pages/article.html',context)


