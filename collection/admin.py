from django.contrib import admin

from collection.models import Hike

class HikeAdmin(admin.ModelAdmin):
    model = Hike
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Hike, HikeAdmin)
