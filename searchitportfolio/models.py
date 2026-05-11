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

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectAsset(models.Model):

    ASSET_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('pdf', 'PDF'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='assets'
    )

    file = models.FileField(upload_to='projects/assets/')

    asset_type = models.CharField(
        max_length=10,
        choices=ASSET_TYPES
    )

    featured = models.BooleanField(default=False)

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset_type} for {self.project.title}"