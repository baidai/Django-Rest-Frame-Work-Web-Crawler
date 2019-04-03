from django.contrib import admin

from .models import Subject, Author, Article
# Register your models here.
admin.site.register(Subject)

# Register your models here.
admin.site.register(Author)

admin.site.register(Article)