from django.contrib import admin

# Register your models here.
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'picture']

admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'product', 'description_reviews', 'grade', 'moderated']

admin.site.register(Review, ReviewAdmin)