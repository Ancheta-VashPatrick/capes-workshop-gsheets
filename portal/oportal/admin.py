from django.contrib import admin
from .models import Opportunity

#admin.site.register(Opportunity)

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'status', 'location',) # Details present in the admin page's opportunity list/table

    #fields = ['role', 'status', ('location', 'opportunity_type')]
    list_filter = ('status', 'opportunity_type') # Available filters in the admin page's opportunity list/table

    search_fields = ('role',) # Search bar to find specific roles

    # Groups the fields by the provided fieldsets
    fieldsets = (
        ('Fieldset 1', {
            'fields': ('role', 'status', 'location')
        }),
        ('Fieldset 2', {
            'fields': (('duration', 'company'), 'description')
        }),
    )

admin.site.register(Opportunity, OpportunityAdmin)