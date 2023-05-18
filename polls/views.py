from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello, world. You're at the poll index")
    return render(request, 'polls/home.html')

def about(request):
    # return HttpResponse("Hello, world. You're at the poll index")
    return render(request, 'polls/about.html')

#canfdjjas

