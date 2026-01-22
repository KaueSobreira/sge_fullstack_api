from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name',)


admin.site.register(Brand, BrandAdmin)
