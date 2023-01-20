from django.db import models
from django.contrib.auth.models import AbstractUser 

'''
Custom user model which has boolean values indicating if the user is a company or student
'''
class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

'''
Model for a company
'''
class Company(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE, # Company will be deleted once their corresponding user is also deleted
        null=True, # Allows null values
        blank=True, # Allows null values in your forms including the admin page
    )
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