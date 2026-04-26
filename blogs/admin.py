from django.contrib import admin
from . import models

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','status','is_featured',)
    search_fields = ('title','category__category_name','status',)
    list_editable = ('is_featured',)

admin.site.register(models.Category)
admin.site.register(models.Blog,BlogAdmin)