from django.http import HttpResponse
from django.shortcuts import render
from oportal.models import Opportunity

"""
Function-based view which returns a page with 'Hello World'
"""
# def home(request):
#     return HttpResponse('Hello World') # Returns a simple web page with the text 'Hello World'

"""
Function-based view which returns the home page
"""
def home(request):
    names = ["Anonymous", "User"]

    num_opportunities = Opportunity.objects.all().count() # Gets the number of opportunities

    num_internships = Opportunity.objects.filter(opportunity_type__exact='INTERNSHIP').count() # Gets the number of internship opportunities

    context = {
        'names' : names,
        'num_opportunities' : num_opportunities,
        'num_internships' : num_internships,
    }

    return render(request, 'home.html', context) # Returns 'home.html' with provided context