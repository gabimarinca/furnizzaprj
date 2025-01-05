from django.urls import path
from core.views import index,about,contact, product_list_view, category_list_view, category_product_list_view
from core import views
app_name = "core"

urlpatterns =[
    path("home/",index,name="index"),
    path("about/",views.about),
    path("contact/",views.contact),
    path("products/", product_list_view, name = "product-list"),
    path("categories/", category_list_view, name = "category-list"),
    path("categories/<categoryid>/", category_product_list_view, name = "category-product-list"),
] 