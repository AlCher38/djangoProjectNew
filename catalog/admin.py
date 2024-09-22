from django.contrib import admin

from catalog.models import Category, Product


# admin.site.register(Student)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
