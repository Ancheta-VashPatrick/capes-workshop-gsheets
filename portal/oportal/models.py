from django.db import models
from django.urls import reverse 

from model_utils import Choices
from accounts.models import Company

'''
Model for an opportunity
'''
class Opportunity(models.Model):    
    role = models.CharField(max_length=40)

    OPP_STATUS = (
        ('New', 'n'),
        ('Closing Soon', 'c'),
        ('Expired', 'e'),
    )

    status = models.CharField(
        max_length=20,
        choices=OPP_STATUS,
        null=True, # Allows null values
        blank=True, # Allows null values in your forms including the admin page
        help_text='Opportunity status',
    )

    LOCATIONS = Choices('Local', 'International')

    location = models.CharField(choices=LOCATIONS, max_length=40)

    OPPORTUNITY_TYPES = Choices('INTERNSHIP', 'ACADEME', 'EMPLOYMENT')

    opportunity_type = models.CharField(choices=OPPORTUNITY_TYPES, max_length=40)

    duration = models.CharField(max_length=40)
    
    description = models.TextField(
        default="Insert description here"
    )
    
#    company = models.ForeignKey(Company, on_delete=models.SET_NULL) # NULL will set the opportunities' 'company' field to null if their related company is deleted 
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # CASCADE will delete all opportunities if their related company is deleted

    # String representation of the model
    def __str__(self):
        return self.role + " : " + self.company.name

    # Returns url for opportunity page with the primary key 'pk' as argument
    def get_absolute_url(self):
        # return reverse('opportunity', args=[str(self.id)])
        return reverse('opportunity', kwargs={'pk' : self.id}) # Using keyword arguments to supply the URL arguments

    # Returns url for updating an opportunity page with the primary key 'pk' as argument
    # Note that this function is not used since passing of arguments is done in the opportunity.html template
    # This function is only for demonstration
    def get_update_url(self):
        return reverse('opportunity-update', args=[str(self.id)])

    # Returns url for opportunity page with the primary key 'pk' as argument
    # Note that this function is not used since passing of arguments is done in the opportunity.html template
    # This function is only for demonstration
    def get_delete_url(self):
        return reverse('opportunity-delete', args=[str(self.id)])

    class Meta:
        ordering = ['role'] # Sort by role (alphabetically)
        verbose_name_plural = 'Opportunities'
        
        # Adding custom permissions
        permissions = (
            ("can_add_opportunity", "Add opportunity"),
            ("can_edit_opportunity", "Edit opportunity"),
            ("can_delete_opportunity", "Delete opportunity"),
        ) 