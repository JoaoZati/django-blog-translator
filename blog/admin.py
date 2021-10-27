from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_create', 'author')


admin.site.register(Post, PostAdmin)


