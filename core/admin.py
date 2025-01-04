from django.contrib import admin
from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, Review, Wishlist, Address
 
# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'productImage', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['title', 'categoryImage']

class VendorAdmin(admin.ModelAdmin): 
    list_display = ['title', 'vendorImage']

class CartOrderAdmin(admin.ModelAdmin): 
    list_display = ['user', 'price', 'paid_status', 'date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin): 
    list_display = ['order', 'invoice', 'item', 'image', 'quantity', 'price', 'total']

class ReviewAdmin(admin.ModelAdmin): 
    list_display = ['user', 'product', "comment", "rating"]

class WishlistAdmin(admin.ModelAdmin): 
    list_display = ['user', 'product', 'date']

class AddressAdmin(admin.ModelAdmin): 
    list_display = ['user', 'street', 'city', 'zipCode', 'country', 'status']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)

