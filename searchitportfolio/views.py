# Create your views here.

from django.shortcuts import render
from .models import Project, MediaType, ClientType

def home(request):
    projects = Project.objects.all()
    media_types = MediaType.objects.all()
    client_types = ClientType.objects.all()

    return render(request, 'home.html', {
        'projects': projects,
        'media_types': media_types,
        'client_types': client_types,
    })