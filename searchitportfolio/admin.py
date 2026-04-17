# Register your models here.
from django.contrib import admin
from .models import Project, MediaType, ClientType, ProjectAsset

class ProjectAssetInline(admin.TabularInline):
    model = ProjectAsset
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectAssetInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(MediaType)
admin.site.register(ClientType)

