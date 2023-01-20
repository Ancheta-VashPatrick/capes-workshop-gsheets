from django.test import TestCase
from django.contrib.auth.models import Permission
from django.urls import reverse

from accounts.models import CustomUser, Company

from oportal.forms import UpdateOpportunityForm
from .. import views
from ..models import Opportunity


"""
Test case for the update opportunity function-based view
"""
class UpdateOpportunityViewTest(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='test1', password='123')
        edit_permission = Permission.objects.get(codename="can_edit_opportunity")
        user1.user_permissions.add(edit_permission)
        user2 = CustomUser.objects.create_user(username='test2', password='123')

        company1 = Company.objects.create(name="UP CAPES 1", logo = None, user=user1)
        company2 = Company.objects.create(name="UP CAPES 2", logo = None, user=user2)

        self.opp1 = Opportunity.objects.create(
            role="Developer", 
            status="New", 
            location="Local", 
            opportunity_type="INTERNSHIP", 
            duration="August - September", 
            company=company1,
        )

        self.opp2 = Opportunity.objects.create(
            role="Senior Developer", 
            status="New", 
            location="Local", 
            opportunity_type="INTERNSHIP", 
            duration="August - September", 
            company=company2,
        )

    # Checks if the user has the permissions to update an opportunity by checking if the proper template is rendered
    # This test will fail because the opportunity 'opp2' belongs to the company 'UP CAPES 2' which is only accessible by user 'test2'
    def test_permissions(self):
        self.client.login(username='test1', password='123')
        response = self.client.get(reverse('opportunity-update', kwargs={'pk' : self.opp2.pk })) # GET response

        self.assertTemplateUsed(response, 'oportal/opportunity_form.html') 

    # Checks if the form's initial fields were prefilled for an existing opportunity by checking the role field
    # This test will succeed
    def test_form_prefilled_fields(self):
        self.client.login(username='test1', password='123')
        
        response = self.client.get(reverse('opportunity-update', kwargs={'pk' : self.opp1.pk })) # GET response
        form = response.context.get('form') # Gets the form
        role = form.initial.get('role') # Gets the initial values of the form

        self.assertEqual(role, 'Developer') 

    # Checks if saving the form is able to update an opportunity object
    # This test will succeed
    def test_update_opportunity(self):
        self.client.login(username='test1',password='123')

        response = self.client.get(reverse('opportunity-update', kwargs={'pk' : self.opp1.pk })) # GET response
        form = response.context.get('form')
        form.initial.update({ 'role' : 'Senior Developer' }) # Fills the form programatically
        data = form.initial

        response = self.client.post(reverse('opportunity-update', kwargs={'pk' : self.opp1.pk }), data=data) # POST response
        self.opp1.refresh_from_db() # Reloads opp1 with the values in the database

        self.assertEqual(self.opp1.role, 'Senior Developer') 
        

