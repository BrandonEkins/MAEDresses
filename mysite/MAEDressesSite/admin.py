# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin

from .models import Address, Billinginformation, Cart, Cartedproduct, Customer, Neworder, Product, Staff, Wholesaler

# Register your models here.
admin.site.register(Address)
admin.site.register(Billinginformation)
admin.site.register(Cart)
admin.site.register(Cartedproduct)
admin.site.register(Customer)
admin.site.register(Neworder)
admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Wholesaler)