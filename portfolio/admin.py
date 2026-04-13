from django.contrib import admin

from .models import Category, PortfolioItem, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'date_created']
    list_filter = ['category', 'featured', 'tags']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']
