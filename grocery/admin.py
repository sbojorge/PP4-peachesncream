from django.contrib import admin
from .models import Grocery


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'created_on'
    )

    list_filter = ('author', 'created_on')
