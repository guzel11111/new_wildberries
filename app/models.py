from django.contrib.auth.models import AbstractUser 
from django.db import models

from django.conf import settings
from django.utils.text import slugify



class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


class Cart(models.Model):
    session_key = models.CharField(max_length=40, null=True, blank=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Product(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=200,
    )
    desc = models.TextField(
        verbose_name="Описание",
        max_length=600,
    )

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10, 
        decimal_places=2,
        )

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="products/",
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        "Brand",
        verbose_name="Бренд",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        "URL",
        max_length=250,
        unique=True, 
        null=True,
        editable=True,
    )


    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        "URL", 
        max_length=250,
        unique=True, 
        null=True,
        editable=True,
    )
    
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    site_url = models.URLField(
        verbose_name="Ссылка на сайт",
        max_length=200,
    )

    country = models.CharField(
        verbose_name="Страна",
        max_length=200,
    )
    class Meta:
        verbose_name="Бренд"
        verbose_name_plural="Бренды"

    def __str__(self):
        return self.name
    
    # price 
    # brand 
    # name
    # category
    # desc
    # image

# Create your models here.
