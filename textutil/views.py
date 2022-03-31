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

def ex1(request):

 '''s= <h2>Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
   # <a href="https://www.google.com/"> Google </a> <br>
    reutrn HttpResponse(s)'''
    #sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
   # return HttpResponse((sites))

 def analyzed(request):
    djtext = request.GET.get('text','defualt')
    removepunc = request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
    #analyze = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    params = {'purpose': 'changed to upper', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
    elif fullcaps == "on"
    analyzed = ""
    for char in djtext:
        #analyzed = analyzed + char.upper()

    else
    return HttpResponse('Error')
    #params ={'purpose':'remove punctuations','analyzed text':'analyze'}
    #return render(request,'analyze.html',params)
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





