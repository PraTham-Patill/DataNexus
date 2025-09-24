from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'created_at')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
