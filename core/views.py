from django.http import HttpResponse
from django.shortcuts import render
from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, Review, Wishlist, Address
 
# Create your views here.
def index(request):
   #products = Product.objects.all().order_by("-id")
   products = Product.objects.filter(product_status = "published")
   context = {
      "products" : products
   }
   return render(request, "core/index.html", context)
    #return HttpResponse("<h1>Welcome to Furnizzzzza!</h1>")
    #pass

def product_list_view(request):
   #products = Product.objects.all().order_by("-id")
   products = Product.objects.filter(product_status = "published")
   context = {
      "products" : products
   }
   return render(request, "core/product-list.html", context)

def category_list_view(request):
   #products = Product.objects.all().order_by("-id")
   categories = Category.objects.all()
   context = {
      "categories" : categories
   }
   return render(request, "core/category-list.html", context)

def category_product_list_view(request, categoryid): # 2nd is for 2nd
   category = Category.objects.get(categoryid = categoryid)
   products = Product.objects.filter(product_status = "published", category=category)
   
   context = {
      "category": category,
      "products" : products
   }
   return render(request, "core/category-product-list.html", context)


def about(request):
   return render(request, "core/about.html")
def contact(request):
   return render(request, "core/contact.html")