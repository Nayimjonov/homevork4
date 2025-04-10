from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name