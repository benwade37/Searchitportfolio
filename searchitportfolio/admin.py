from django.contrib import admin
from .models import Project, MediaType, ClientType

admin.site.register(Project)
admin.site.register(MediaType)
admin.site.register(ClientType)
# Register your models here.
