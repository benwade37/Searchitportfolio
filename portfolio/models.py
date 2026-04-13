from django.db import models
from django.urls import reverse


class Category(models.Model):
    CODING = 'coding'
    ADVERTISING = 'advertising'
    DESIGN = 'design'
    OTHER = 'other'

    CATEGORY_CHOICES = [
        (CODING, 'Coding'),
        (ADVERTISING, 'Advertising'),
        (DESIGN, 'Design'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.get_name_display()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items',
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='items')
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    url = models.URLField(blank=True, help_text='External link for this project')
    date_created = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:item_detail', kwargs={'pk': self.pk})
