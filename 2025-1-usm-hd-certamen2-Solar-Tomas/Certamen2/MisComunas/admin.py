from django.contrib import admin
from .models import Comuna
# Register your models here.

@admin.register(Comuna)
class comunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('id',)