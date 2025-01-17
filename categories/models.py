from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Add a description field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name