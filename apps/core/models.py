from django.db import models


class Person(models.Model):
    person_name = models.CharField('person name', max_length=100)
    phone = models.CharField('phone', max_length=20)


class Product(models.Model):
    product_name = models.CharField('product name', max_length=100)
    category = models.CharField('category', max_length=100)
