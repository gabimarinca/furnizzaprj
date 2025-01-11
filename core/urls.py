from django.urls import path
from core.views import add_to_cart,ajax_add_review, index,about,contact, product_list_view, category_list_view, category_product_list_view, vendor_detail_view, vendor_list_view, product_detail_view
from core import views
app_name = "core"

urlpatterns =[
    path("home/",index,name="index"),
    path("about/",views.about),
    path("contact/",views.contact),

    path("products/", product_list_view, name = "product-list"),
    path("product/<prodid>", product_detail_view, name = "product-detail"), 
    path("categories/", category_list_view, name = "category-list"),
    path("categories/<categoryid>/", category_product_list_view, name = "category-product-list"),

    path("vendors/", vendor_list_view, name = "vendor-list"),
    path("vendors/<vendorid>", vendor_detail_view, name = "vendor-detail"),
    
    path("add-to-cart/", add_to_cart, name = 'add-to-cart'),
    
    path("ajax-add-review/<prodid>", ajax_add_review,name = "ajax-add-review")
] 