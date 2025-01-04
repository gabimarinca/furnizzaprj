from django.urls import path
from core.views import index,about,contact
from core import views
app_name = "core"

urlpatterns =[
    path("home/",index,name="index"),
    path("about/",views.about),
    path("contact/",views.contact)
] 