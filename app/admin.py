from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
from .models import Product, Category, Brand
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)