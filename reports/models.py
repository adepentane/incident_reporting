from django.db import models
from django.conf import settings
from categories.models import Category
from django.utils.text import slugify
import bleach
from ckeditor.fields import RichTextField
from cities_light.models import Country, Region, SubRegion

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = RichTextField(config_name='default')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    lga = models.ForeignKey(SubRegion, on_delete=models.SET_NULL, null=True, blank=True)
    street_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    revisions = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Report by {self.user.username} in {self.category.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.description = self.clean_description(self.description)
        if self.pk:
            self.revisions += 1
        super().save(*args, **kwargs)

    def clean_description(self, description):
        allowed_tags = [
            'b', 'i', 'u', 'ul', 'ol', 'li'
        ]
        cleaned_description = bleach.clean(
            description, tags=allowed_tags, strip=True
        )
        return cleaned_description

class Image(models.Model):
    report = models.ForeignKey(Report, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reports/images/')

    def __str__(self):
        return f"Image for {self.report}"

class Video(models.Model):
    report = models.ForeignKey(Report, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='reports/videos/')

    def __str__(self):
        return f"Video for {self.report}"
