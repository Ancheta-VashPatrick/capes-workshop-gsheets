from django.db import models
from django.contrib.auth.models import AbstractUser

from gsheets import mixins


class CustomUser(AbstractUser):
    '''
    Custom user model which has boolean values indicating if the user is a company or student
    '''
    is_company = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Company(mixins.SheetSyncableMixin, models.Model):
    '''
    Model for a company
    '''
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE, # Company will be deleted once their corresponding user is also deleted
        null=True, # Allows null values
        blank=True, # Allows null values in your forms including the admin page
    )
    spreadsheet_id = '1xQdwE8OyFo09mv8KnW50nCUxzXcPG9BC0MhAOCTYZ5s'
    sheet_name = 'Companies'

    name = models.CharField(max_length=40)

    logo = models.FileField(
        upload_to='opps_logos',
        null=True,
        blank=True,
    )

    # String representation of the model
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'
