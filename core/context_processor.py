from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, Review, Wishlist, Address
 

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    address = Address.objects.get(user = request.user)

    return {
        'categories' : categories,
        'vendors' : vendors,
        'address' : address,
    }