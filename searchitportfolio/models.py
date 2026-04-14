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