from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)  #changed wed,8:20

class Category(models.Model):
    name=models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
         return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product',on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()



    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    

    
    

