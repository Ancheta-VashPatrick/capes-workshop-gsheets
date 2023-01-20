from django import forms
from .models import Opportunity

'''
Form for creating an opportunity
'''
class CreateOpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        exclude = ('company',) # Excludes the 'company' field so that users cannot create opportunities from other companies

'''
Form for updating an opportunity
'''
class UpdateOpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        exclude = ('company',) # Excludes the 'company' field so that users cannot update opportunities from other companies