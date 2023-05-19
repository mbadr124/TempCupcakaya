from django.contrib import admin
from .models import Item, OrderItem, Order, Flavours, Toppings, Option, Coverage, Amount, Shape, User
# Register your models here.

admin.site.register (Flavours)
admin.site.register (Toppings)
admin.site.register (Option)
admin.site.register (Coverage)
admin.site.register (Amount)
admin.site.register (Item)
admin.site.register (OrderItem)
admin.site.register (Order)
admin.site.register (Shape)
admin.site.register (User)