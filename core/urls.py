from django.urls import path
from. views import (
    homeview,
    productview,
    add_to_cart
)


urlpatterns = [
    path('',homeview.as_view(),name='home'),
    path('product/<slug>/',productview.as_view(),name='product'),
    path('add_to_cart/<slug>/',add_to_cart,name='add_to_cart')
]