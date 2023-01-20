from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from gsheets.signals import sheet_row_processed

from accounts.models import Company
from .models import Opportunity


@receiver(sheet_row_processed, sender=Opportunity)
def tie_opportunity_to_company(instance=None, created=None, row_data=None, **kwargs):
    try:
        instance.company = Company.objects.get(
            name__iexact=row_data['company_name'])
        instance.save()
    except (ObjectDoesNotExist, KeyError):
        pass
