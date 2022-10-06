from random import choices
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models
from django.conf import settings
from django.shortcuts import reverse,redirect

# Create your models here.
CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sportwear'),
    ('OW','Outwear'),
)

LABEL_CHOICES=(
    ('P','Primary'),
    ('S','Secondary'),
    ('D','Danger'),
)

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField(null=True,blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    label=models.CharField(choices=LABEL_CHOICES,max_length=1)
    slug=models.SlugField()
    description=models.TextField(max_length=1000)

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product',kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('add_to_cart',kwargs={
            'slug': self.slug
        })


    


class OrderItem(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,blank=True,null=True)
    ordered=models.BooleanField(default=False)                         
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)



class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
items=models.ManyToManyField(OrderItem)
start_date=models.DateTimeField(auto_now=True)     
ordered_date=models.DateTimeField()                               
ordered=models.BooleanField(default=False)
