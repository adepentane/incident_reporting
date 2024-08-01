from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'country', 'state', 'created_at', 'is_active')
    list_filter = ('category', 'country', 'state', 'is_active')
    search_fields = ('description', 'user__username', 'category__name', 'country', 'state', 'lga', 'street_name')
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = 'Mark selected reports as active'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = 'Mark selected reports as inactive'