from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, Review, Wishlist, Address
from django.db.models import Avg
from core.forms import ReviewForm
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


def vendor_list_view(request):
   vendors = Vendor.objects.all()
   context = {
      'vendors' : vendors
   }
   return render(request, "core/vendor-list.html", context)



def vendor_detail_view(request, vendorid):
   vendor = Vendor.objects.get(vendorid = vendorid)
   products = Product.objects.filter(product_status = "published", vendor = vendor)
   context = {
      'vendor' : vendor,
      'products' : products,
   }
   return render(request, "core/vendor-detail.html", context)


def product_detail_view(request,prodid):
   product = Product.objects.get(prodid = prodid)
   #product = get_object_or_404(Product, prodid = prodid)
   products = Product.objects.filter(category = product.category).exclude(prodid = prodid)
   
   reviews = Review.objects.filter(product = product).order_by("-date")
   review_form = ReviewForm()

   average_rating = Review.objects.filter(product = product).aggregate(rating = Avg('rating'))

   context = {
      "average_rating" : average_rating,
      "product" : product,
      "products" : products,
      "reviews" : reviews,
      "review_form" : review_form,
   }
   return render(request, "core/product-detail.html", context)


def about(request):
   return render(request, "core/about.html")

def contact(request):
   return render(request, "core/contact.html")

def ajax_add_review(request, prodid):



   product = Product.objects.get(pk = prodid)
   user = request.user

   comment = ReviewForm.objects.create(
      user = user,
      product = product,
      comment = request.POST['comment'],
      rating = request.POST['rating'],
   )

   context = {
      'user' : user.username,
      'comment' : request.POST['comment'],
      'rating' :request.POST['rating'],  
   }

   average_reviews =Review.objects.filter(product = product).aggregate(rating = Avg("rating"))
   
   return JsonResponse(
      {
      'bool' : True,
      'context' : context,
      'average_reviews' : average_reviews
      }
   )

def add_to_cart(request):  
   cart_product = {}

   cart_product[str(request.GET['id'])] = {
      'title': request.GET['title'],
      'quantity' : request.GET['quantity'],
      'price' : request.GET['price'],
      'image' : request.GET['image'],
      'prodid' : request.GET['prodid'],
      
   }
   if 'cart_data_obj' in request.session:
      if str(request.GET['id']) in request.session['cart_data_obj']:
         cart_data = request.session['cart_data_obj']
         cart_data[str(request.GET['id'])]['quantity'] = int(cart_product[str(request.GET['id'])]['quantity'])
         cart_data.update(cart_data)
         request.session['cart_data_obj'] = cart_data
      else:
         cart_data= request.session['cart_data_obj']
         cart_data.update(cart_product)
         request.session['cart_data_obj'] = cart_data
   else:
      request.session['cart_data_obj'] = cart_product
   return JsonResponse({"data": request.session['cart_data_obj'], 'totalcartitems' : len(request.session['cart_data_obj'])})