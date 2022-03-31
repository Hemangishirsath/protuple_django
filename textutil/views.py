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




 def analyzed(request):
    djtext = request.GET.get('text','defualt')
    removepunc = request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    print(removepunc)
    print(djtext)
    analyzed = ""
    for char in djtext:

            analyzed = analyzed + char
    params = {'purpose': 'changed to upper', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
    #params ={'purpose':'remove punctuations','analyzed text':'analyze'}
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
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





