from django.contrib import admin

from .models import Project, Comment, Category, Picture

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Picture)

