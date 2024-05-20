from django.contrib import admin
from .models import Book
# Register your models here.

class BookFields(admin.ModelAdmin):
    list_display = ('id','title','author','genre','published_year','isbn','publisher','pages','language','description','cover_image_url','status')

admin.site.register(Book,BookFields)