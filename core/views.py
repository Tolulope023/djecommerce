from genericpath import exists
from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from .models import Item, OrderItem,Order
from django.utils import timezone
# Create your views here.

class homeview(ListView):
    model=Item
    template_name='home-page.html'

class productview(DetailView):
    model=Item
    template_name='product-page.html'


def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item=OrderItem.objects.get_or_create(item=item)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs

        if order.objects.filter(item_slug=item.slug).exists:
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        return redirect('product',slug=slug)