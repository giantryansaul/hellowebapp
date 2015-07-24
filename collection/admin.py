from django.contrib import admin

from collection.models import Hike, Profile

class HikeAdmin(admin.ModelAdmin):
    model = Hike
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hike, HikeAdmin)
