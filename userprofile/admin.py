from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','cc_points','year','branch','college','mobile') 
    search_fields = ('user','college','branch')
    list_filter = ('user','cc_points','college','branch','year') #tags cannot be searched

