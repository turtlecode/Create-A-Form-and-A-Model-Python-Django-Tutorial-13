from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
