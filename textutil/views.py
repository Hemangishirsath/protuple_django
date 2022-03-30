#i have creste this file in python
from django.http import HttpResponse
from django.shortcuts import render

#code video 6

#def index(request):
   # return HttpResponse ('''<h1>hello</h1><a href="https://www.amazon.com/shop/sueoverydesigns">django codes</a>''')

# about(request):
    #return HttpResponse (" about hello harry")


def index(request):
    return render(request,'index.html')
    #return HttpResponse("hello")


def analyze(request):
    djtext = request.GET.get('text','defualt')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    analyze = djtext
    params ={'purpose':'remove punctuations','analyzed text':'analyze'}
    return render(request,'analyze.html',params)
    #return HttpResponse("remove punc")
'''

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")
   
    '''





