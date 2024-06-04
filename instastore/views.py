from django.shortcuts import render
from django.http import HttpResponse  

# Http is a module, not a class.(a package)
# HttpResponse is a class, so we need to instantiate it.
# Create your views here.

def say_hello(request):
    return render(request, 'description.html')


# map this request to a URL so that when i get a request to this URL,this function will be called
