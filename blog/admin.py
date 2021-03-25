from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/tinyinject.js",)

admin.site.register(Post, PostAdmin)
