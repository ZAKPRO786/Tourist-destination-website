from django.contrib import admin
from .models import TouristDestination


class TouristDestinationAdmin(admin.ModelAdmin):
    # List of fields to display in the admin list view
    list_display = ('place_name', 'state', 'district', 'weather')

    # Fields that you can search through in the admin panel
    search_fields = ('place_name', 'state', 'district', 'weather')

    # Filters for narrowing down destinations based on state or district
    list_filter = ('state', 'district')

    # Enable editing of these fields directly in the list view
    list_editable = ('weather',)

    # Order the displayed list by a specific field (e.g., place name)
    ordering = ('place_name',)


# Register the TouristDestination model with the customized admin interface
admin.site.register(TouristDestination, TouristDestinationAdmin)

