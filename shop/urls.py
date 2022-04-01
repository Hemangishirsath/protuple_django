from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about",views.index,name="AboutUs"),
    path("contact",views.contact,name="ContactUs"),
    path("tracker",views.tracker,name="trackingStatus"),
    path("search",views.search,name="search"),
    path("product",views.product,name="Product"),
    path("checkout",views.checkout,name="Checkout"),

]