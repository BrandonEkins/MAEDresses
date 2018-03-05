# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Address(models.Model):
    addressid = models.BigAutoField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    astate = models.CharField(db_column='aState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'

class Billinginformation(models.Model):
    billinginformationid = models.BigAutoField(db_column='BillingInformationID', primary_key=True)  # Field name made lowercase.
    creditcardnumber = models.IntegerField(db_column='CreditCardNumber', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'billinginformation'

class Cart(models.Model):
    cartid = models.BigAutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    numberofitems = models.IntegerField(db_column='NumberOfItems', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.FloatField(db_column='TotalCost', blank=True, null=True)  # Field name made lowercase.
    shippingcost = models.FloatField(db_column='ShippingCost', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'

class Cartedproduct(models.Model):
    cartedproductid = models.BigAutoField(db_column='CartedProductID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cartedproduct'

class Customer(models.Model):
    customerid = models.BigAutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='Pass', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    billinginformationid = models.ForeignKey(Billinginformation, models.DO_NOTHING, db_column='BillingInformationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

class Neworder(models.Model):
    neworderid = models.BigAutoField(db_column='NewOrderID', primary_key=True)  # Field name made lowercase.
    cartid = models.ForeignKey(Cart, models.DO_NOTHING, db_column='CartID', blank=True, null=True)  # Field name made lowercase.
    staffid = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'neworder'


class Product(models.Model):
    productid = models.BigAutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    shippingcost = models.FloatField(db_column='ShippingCost', blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    wholesalerid = models.ForeignKey('Wholesaler', models.DO_NOTHING, db_column='WholesalerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class Staff(models.Model):
    staffid = models.BigAutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    staffname = models.CharField(db_column='StaffName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wage = models.IntegerField(db_column='Wage', blank=True, null=True)  # Field name made lowercase.
    spassword = models.CharField(db_column='sPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'


class Wholesaler(models.Model):
    wholesalerid = models.BigAutoField(db_column='WholesalerID', primary_key=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wholesalername = models.CharField(db_column='WholesalerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wholesalerphone = models.CharField(db_column='WholesalerPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wholesalerlocation = models.CharField(db_column='WholesalerLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wholesaler'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'