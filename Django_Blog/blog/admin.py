from django.contrib import admin
from .models import Post, NameCount

admin.site.register(Post)
admin.site.register(NameCount)