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
    result= articles
    search=request.GET.get('search')
    print(search)
    if search:
        result=[article for article in articles if search.lower() in article.article1.lower()
        ]
    context={
        "data2":"happy to learn context",
        "data3":"this is context ",
        'title': 'article',
        'articles': result,
    }
    return render(request,'pages/contact6.html',context)

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
