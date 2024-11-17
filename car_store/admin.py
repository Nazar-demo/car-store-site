from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'power', 'status')
    prepopulated_fields = {'slug': ('mark', 'model')}


admin.site.register(Car, CarAdmin)
