from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, "core/index.html")
    #return HttpResponse("<h1>Welcome to Furnizzzzza!</h1>")
    #pass
def about(request):
   return render(request, "core/about.html")
def contact(request):
   return render(request, "core/contact.html")