from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator
from django.urls import reverse_lazy

from .models import Opportunity

"""
Function-based view which lists down all opportunities
Function-based view equivalent to the class-based view below
"""
def opportunities(request):
    opportunities = Opportunity.objects.all() # Gets all opportunities
    
    paginator = Paginator(opportunities, 3) # Show 3 opportunities per page
    page_number = request.GET.get('page', 1) # Gets the page number from the GET request arguments or defaults to the first page
    page_obj = paginator.get_page(page_number) # Gets a Page object which is an iterator and if iterated upon, will return the individual opportunities
    opportunities = paginator.page(page_number) # Equivalent to the line above

    context = {
        "opportunities" : opportunities,
        "page_obj" : page_obj,
        "paginator" : paginator,
    }

    return render(request, 'oportal/opportunities.html', context) # Returns 'oportal/opportunities.html' with provided context

"""
Class-based view which lists down all opportunities
Class-based view equivalent to the function-based view above
"""
class OpportunityListView(generic.ListView):
    model = Opportunity # Specifying which model to use in the view
    context_object_name = 'opportunities' # Specifying the name of the variable in the template
    template_name = 'oportal/opportunities.html' # Specifying the location of your template

    # paginate_by = 3 # Defining the number of opportunities per page
    queryset = Opportunity.objects.filter(opportunity_type__contains='INTERNSHIP') # Filtering only the internship opportunities

"""
Class-based view which presents the details of an individual opportunity
"""
class OpportunityDetailView(generic.DetailView):
    model = Opportunity # Specifying which model to use in the view
    template_name = 'oportal/opportunity.html' # Specifying the name of the variable in the template

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import CreateOpportunityForm, UpdateOpportunityForm

""" 
Class-based view which presents a form and upon receiving a valid submission will create a new opportunity
"""
class OpportunityCreateView(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'oportal.can_add_opportunity' # Specifying the permission needed to use the view
    model = Opportunity # Specifying which model to use in the view
    form_class = CreateOpportunityForm # Specifying the form class to use 
    template_name = 'oportal/opportunity_form.html' # Specifying the location of your template

    # Function to execute upon receiving a POST request
    # Note that the post function was overriden in order to prevent the save function from saving the model object directly to the database
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST) # Gets the data from the POST request 

        # Executes if the form passes all validators
        if form.is_valid(): 
            opportunity = form.save(commit=False) # Saving the form using commit=False will return a model object
            opportunity.company = self.request.user.company # Setting the company of the opportunity model to the company of the user
            opportunity.save() # Saving the opportunity model
            return redirect('oportal') # Redirects to the opportunities page

"""
Class-based view which presents a form and upon receiving a valid submission will update an existing opportunity
Almost equivalent to the function-based view below, this view returns a 404 response on unauthorized access to other company's opportunities 
"""
# class OpportunityUpdateView(PermissionRequiredMixin, generic.UpdateView):
#     permission_required = 'oportal.can_edit_opportunity' # Specifying the permission needed to use the view
#     model = Opportunity # Specifying which model to use in the view
#     form_class = UpdateOpportunityForm # Specifying the form class to use 
#     template_name = 'oportal/opportunity_form.html' # Specifying the location of your template
#     
#     # Function which limits the opportunity that the current user can access (only opportunities of the current user's company)
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(company__user=self.request.user) # Gets only the opportunities with its company user equal to the current user
#         return queryset

from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required


""" 
Function-based view which presents a form and upon receiving a valid submission will update an existing opportunity
Almost equivalent to the class-based view above, this view returns a 403 response on unauthorized access to other company's opportunities 
""" 
@login_required # Decorator which requires login before accessing the function-based view
@permission_required('oportal.can_edit_opportunity', raise_exception=True) # Decorator which requires the indicated permission before accessing the view
def update_opportunity(request, pk):
    opportunity = Opportunity.objects.get(pk=pk) # Gets the opportunity based on the primary key provided as argument to the URL
    
    # Condition which limits the opportunity that the current user can access (only opportunities of the current user's company) 
    if(opportunity.company.user != request.user):
        raise PermissionDenied() # Raises error 403

    # Handles the POST request
    if request.method == 'POST':
        form = UpdateOpportunityForm(data=request.POST, instance=opportunity) # The instance is set to the opportunity so that a new model object is not created and the existing opportunity is updated 

        # Executes if the form passes all validators
        if form.is_valid(): 
            form.save() # Saves the model form which will also save a model
            return redirect('oportal') # Redirects to the opportunities page

    # Handles the GET request
    else:
        form = UpdateOpportunityForm(instance=opportunity) # Pre-fills the form with the existing opportunity's details

    context = {
        'form' : form
    }

    return render(request, 'oportal/opportunity_form.html', context=context) # Returns 'oportal/opportunity_form.html' with provided context

"""
Function-based view which presents a form and upon receiving a valid submission will update an existing opportunity
Almost equivalent to the function-based view above, this view uses a custom decorator for permissions
"""
# from accounts.decorators import company_required

# @login_required
# @company_required
# def update_opportunity(request, pk):
#     opportunity = Opportunity.objects.get(pk=pk) # Gets the opportunity based on the primary key provided as argument to the URL

#     # Condition which limits the opportunity that the current user can access (only opportunities of the current user's company) 
#     if(opportunity.company.user != request.user):
#         raise PermissionDenied()
    
#     # Handles the POST request
#     if request.method == 'POST':
#         form = UpdateOpportunityForm(data=request.POST, instance=opportunity) # The instance is set to the opportunity so that a new model object is not created and the existing opportunity is updated 

#         # Executes if the form passes all validators
#         if form.is_valid():
#             form.save() # Saves the model form which will also save a model
#             return redirect('oportal') # Redirects to the opportunities page

#     # Handles the GET request
#     else:
#         form = UpdateOpportunityForm(instance=opportunity) # Pre-fills the form with the existing opportunity's details

#     context = {
#         'form' : form
#     }

#     return render(request, 'oportal/opportunity_form.html', context=context) # Returns 'oportal/opportunity_form.html' with provided context

"""
Class-based view which presents a form and upon submitting will delete the opportunity
"""
class OpportunityDeleteView(PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'oportal.can_delete_opportunity' # Specifying the permission needed to use the view
    model = Opportunity # Specifying which model to use in the view
    template_name = 'oportal/opportunity_confirm_delete.html'  # Specifying the location of your template
    success_url = reverse_lazy('oportal') # Specifying where the page will redirect after a successful deletion
    
    # Function to execute upon receiving a GET request
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk") # Gets the primary key provided as a keyword argument to the URL
        pk = kwargs.get("pk") # Equivalent to the line above

        opportunity = Opportunity.objects.get(pk=pk) # Gets the opportunity based on the primary key

        # Condition which limits the opportunity that the current user can access (only opportunities of the current user's company) 
        if(opportunity.company.user != request.user):
            raise PermissionDenied() # Raises error 403

        context = {
            'opportunity' : opportunity,
        }

        return render(request, template_name = self.template_name, context = context) # Returns 'oportal/opportunity_confirm_delete.html' with provided context

"""
Class-based view which presents a form and upon submitting will delete the opportunity
Almost equivalent to the class-based view above, this view uses a custom decorator for permissions
"""
# from django.utils.decorators import method_decorator  

# from accounts.decorators import company_required

# class OpportunityDeleteView(generic.DeleteView):
#     model = Opportunity # Specifying which model to use in the view
#     template_name = 'oportal/opportunity_confirm_delete.html'  # Specify your own template name/location
#     success_url = reverse_lazy('oportal') # Specifying where the page will redirect after a successful deletion

#     # Handles the GET request but requires login and user has to be a company user
#     @method_decorator([login_required, company_required])
#     def get(self, request, *args, **kwargs):
#         pk = self.kwargs.get("pk") # Gets the primary key provided as a keyword argument to the URL
#         opportunity = Opportunity.objects.get(pk=pk) # Gets the opportunity based on the primary key

#          # Condition which limits the opportunity that the current user can access (only opportunities of the current user's company) 
#         if(opportunity.company.user != request.user):
#             raise PermissionDenied() # Raises error 403

#         context = {
#             'opportunity' : opportunity,
#         }

#         return render(request, template_name = self.template_name, context = context) # Returns 'oportal/opportunity_confirm_delete.html' with provided context