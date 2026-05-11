# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Project, MediaType, ClientType

def home(request):
    projects = Project.objects.prefetch_related('assets', 'media_types', 'client_types').all()

    for project in projects:
        project.first_image = next(
            (asset for asset in project.assets.all() if asset.asset_type == "image"),
            None
        )

    return render(request, 'home.html', {
        'projects': projects,
        'media_types': MediaType.objects.all(),
        'client_types': ClientType.objects.all(),
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})