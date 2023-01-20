from django.test import TestCase

from oportal.models import Opportunity, Company
from accounts.models import CustomUser

"""
Test case for the opportunity model
"""
class OpportunityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(username='test', password='123')
        company = Company.objects.create(name="UP CAPES", logo = None, user=user)

        opp = Opportunity.objects.create(
            role="Developer", 
            status="New", 
            location="Local", 
            opportunity_type="INTERNSHIP", 
            duration="August - September", 
            company=company,
        )

    # Checks if the string representation of an opportunity is of the format 'opportunity role : company name'
    # This test should succeed
    def test_string_representation(self):
        opp = Opportunity.objects.get(role="Developer")
        self.assertEqual(opp.role + " : " + opp.company.name, str(opp))
    
    # Checks if the help text of the status field is equal to the defined help text
    # This test should fail because the actual help text is set to 'Opportunity status'
    def test_status_help_text(self):
        opp = Opportunity.objects.get(role="Developer")
        help_text = opp._meta.get_field('status').help_text
        self.assertEqual(help_text, 'Help!!!')

    # Checks if the function 'get_absolute_url' returns the proper url
    # This test should succeed
    def test_get_absolute_url(self):
        opp = Opportunity.objects.get(role="Developer")
        self.assertEqual(opp.get_absolute_url(), '/oportal/' + str(opp.id) + '/')