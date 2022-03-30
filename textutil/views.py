#i have creste this file in python
from django.http import HttpResponse
from django.shortcuts import render

#code video 6

#def index(request):
   # return HttpResponse ('''<h1>hello</h1><a href="https://www.amazon.com/shop/sueoverydesigns">django codes</a>''')

# about(request):
    #return HttpResponse (" about hello harry")


def index(request):
    params = {'name':'analyzer text','place':'mars'}
    return render(request,'index.html',params)
    #return HttpResponse("home")

def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")





