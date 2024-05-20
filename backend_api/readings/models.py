from django.db import models
import datetime
# Create your models here.

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

    class Meta:
        abstract = True

class Book(DateTimeModel):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255, null = False)
    author = models.CharField(max_length = 255, null = False)
    genre = models.CharField(max_length = 100, null = True)
    published_year = models.IntegerField(null = True)
    isbn = models.CharField(max_length = 13, unique = True)
    publisher = models.CharField(max_length = 255, null = True)
    pages = models.IntegerField(null = True)
    language = models.CharField(max_length = 50, null = True)
    description = models.TextField(null = True)
    cover_image_url = models.URLField(max_length = 255, null = True)
    status = models.BooleanField(default = True)
    def __str__(self):
        return f"{self.title} - {self.author}"