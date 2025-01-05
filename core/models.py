from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
# Create your models here.

STATUS_CHOICE = {
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),

}

STATUS = {
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In_review"),
    ("published", "Published"),
}

RATING = {
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
}



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    categoryid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix= "cat", alphabet= "abcdefghijklmn123456789")
    title = models.CharField(max_length=75, default="Furniture")
    image = models.ImageField(upload_to="category", default="furniture.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def categoryImage(self):
        return mark_safe('<img src="%s" width = "50" height="50"  />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Tags(models.Model):
    pass

class Vendor(models.Model):
    vendorid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix= "ven", alphabet= "abcdefghijklmn123456789")
    
    title = models.CharField(max_length=75, default= "Ikea")
    image = models.ImageField(upload_to="user_directory_path",default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="I am an amazing seller")

    address = models.CharField(max_length=100, default= "Dorobantilor 81, Cluj")
    contact = models.CharField(max_length=100, default= "+40 740 543 123")
    ChatRespTime =models.CharField(max_length=100, default= "100")
    shippingOnTime= models.CharField(max_length=100, default= "100")
    rating = models.CharField(max_length=100, default= "100")
    
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True) # models.CASCADE

    class Meta:
        verbose_name_plural = "Vendors"

    def vendorImage(self):
        return mark_safe('<img src="%s" width = "50" height="50"  />' % (self.image.url))
    
    def __str__(self):
        return self.title

class Product(models.Model):
    prodid = ShortUUIDField(unique=True, length = 10, max_length = 20, prefix= "prod", alphabet= "abcdefghijklmn123456789")
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete = models.SET_NULL,null=True)
    
    title = models.CharField(max_length=75, default="Furniture product")
    image = models.ImageField(upload_to="user_directory_path", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="This is the product!")

    price = models.DecimalField(max_digits=9999999999999,decimal_places=2,default="20.99")
    oldPrice = models.DecimalField(max_digits=9999999999999,decimal_places=2,default="24.99")
    specifications = models.TextField(null=True, blank=True)
    #tags = models.ForeignKey(Tags, on_delete = models.SET_NULL,null=True)
    product_status = models.CharField(choices= STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    


    sku = ShortUUIDField(unique=True, length = 4, max_length = 10, prefix= "sku", alphabet= "1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def productImage(self):
        return mark_safe('<img src="%s" width = "50" height="50"  />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.oldPrice) * 100
        return new_price
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

#---------------------------------------------Cart, Order, OrderItems -------------------------------------------------------

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=9999999999999,decimal_places=2,default="20.99")
    paid_status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices= STATUS_CHOICE, max_length=10, default="processing")
    
    class Meta:
        verbose_name_plural = "Cart Order"

    
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice = models.CharField(max_length=300)
    product_status = models.CharField(max_length=100)
    item =  models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999999,decimal_places=2,default="20.99")
    total = models.DecimalField(max_digits=9999999999999,decimal_places=2,default="20.99")
    
    class Meta:
        verbose_name_plural = "Cart Order Items"

    def orderImage(self):
        return mark_safe('<img src="/media/%s" width = "50" height="50"  />' % (self.image))
    

    #--------------------------Product Review, WishList, Address--------------------------------

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL,null=True)
    comment = models.TextField()
    rating = models.IntegerField(choices= RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
            return self.product.title
    
    def get_rating(self):
        return self.rating
        

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"

    def __str__(self):
            return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipCode = models.PositiveIntegerField(default=None)
    country = models.CharField(max_length=100)

    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Address"

