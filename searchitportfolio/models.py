from django.db import models

class MediaType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ClientType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    media_types = models.ManyToManyField(MediaType)
    client_types = models.ManyToManyField(ClientType)

    cover_image = models.ImageField(upload_to='projects/covers/')
    pdf = models.FileField(upload_to='projects/pdfs/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ProjectAsset(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='assets')
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    pdf = models.FileField(upload_to='projects/pdfs/', blank=True, null=True)

    def __str__(self):
        return f"Asset for {self.project.title}"