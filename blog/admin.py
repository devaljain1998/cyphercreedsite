from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_date','author')
    list_filter = ('published_date','author',)