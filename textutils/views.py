# I have created this file-harryhttps://github.com/Hemangishirsath/protuple_django.git
from django.http import HttpResponse
def index(reuest):
    return  HttpResponse("hello")


def about(request):
    return HttpResponse("bay")