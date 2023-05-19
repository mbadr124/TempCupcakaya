from django.conf import settings
from django.db import models
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


CATEGORY_CHOICES = (
    ('Ck','Cake'),
    ('Cup','Cupcake'),
    ('Cp','Cakepop'),
    ('Co','Cookie')
)


class Flavours(models.Model):
    flav_id = models.IntegerField(null=True, blank=True)
    flavour = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.FloatField(null=True)
    def __str__(self):
        return self.flavour
   


class Toppings(models.Model):
    top_id = models.IntegerField(null=True, blank=True)
    topping = models.CharField (max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.FloatField(null=True)
    def __str__(self):
        return self.topping
    

class Option(models.Model):
    opt_id = models.IntegerField(null=True, blank=True)
    option = models.CharField (max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.FloatField(null=True)
    def __str__(self):
        return self.option
    

class Coverage(models.Model):

    cove_id = models.IntegerField(null=True, blank=True)
    coverage = models.CharField (max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.FloatField(null=True)
    def __str__(self):
        return self.coverage
    
class Shape(models.Model):
    shape_id = models.IntegerField(null=True, blank=True)
    shape = models.CharField (max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    price = models.FloatField(null=True)
    def __str__(self):
        return self.shape
   

class Amount(models.Model):
    amo_id = models.IntegerField(null=True, blank=True)
    amount = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, null=True)
    price = models.FloatField(null=True)
    def __str__(self):
        return self.amount
       
class Item(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15, null=True, blank=True )
    flavour = models.ForeignKey(Flavours, on_delete=models.CASCADE, blank=True, null=True)
    topping = models.ForeignKey(Toppings, null=True, blank=True, on_delete=models.CASCADE)
    option = models.ForeignKey(Option,  null=True, blank=True, on_delete=models.CASCADE)
    coverage = models.ForeignKey(Coverage,null=True,blank=True, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape,null=True,blank=True, on_delete=models.CASCADE)
    amount = models.ForeignKey(Amount, null=True, blank=True, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    image = models.ImageField(null=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.category}-{self.id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"item created: {self.slug}"
    


    


    



    

class User(models.Model):

    username = models.CharField(null=True, max_length=100)
    name= models.CharField(null=True, max_length=100)
    lname = models.CharField(null=True, max_length=100)
    number = models.CharField(null=True, max_length=100)
    country = models.CharField(null=True, max_length=100)
    address = models.CharField(null=True, max_length=100)
    comment = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name
    

class OrderItem (models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Orderitem"
    
    

class Order (models. Model):
    user = models.ForeignKey(User,
    on_delete=models. CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    
    ordered_date = models.DateTimeField(null=True)
    ordered = models. BooleanField(default=False)
    def __str__(self):
        return f"this is order"
    