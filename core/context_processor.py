from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, Review, Wishlist, Address
from django.db.models import Max,Min
 

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all() 
    address = None
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            address = None 
    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))
    return {
        'categories' : categories,
        'vendors' : vendors,
        'address' : address,
        'min_max_price' : min_max_price,

    }