from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm

"""
Function-based view which presents the login form and handles the login of a user
"""
def signin(request):
    next = request.GET.get('next') # Gets the 'next' GET argument

    # Handles the POST request
    if request.method == 'POST': 
        form = LoginForm(data=request.POST) # Gets the data from the POST request 

        # Executes if the form passes all validators
        if form.is_valid():
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password) # Verifies if the provided username and password are valid then returns corresponding user with provided username and password

            login(request, user) # Logs in the user
            if next:
                return redirect(next) # Redirects the page to the url set in the 'next' variable 

    # Handles the GET request
    else:
        form = LoginForm(initial={'username': 'serge'}) # Sets initial username to serge

    context = {
        'form' : form,
        'next' : next,
    }
    
    return render(request, 'accounts/login.html', context) # Returns "accounts/login.html" with provided context

def signout(request):
    logout(request) # Logs out the user
    return render(request, 'accounts/logout.html') # Returns "accounts/logout.html" with provided context

from django.views import generic
from .forms import RegistrationForm

"""
Class-based view which presents the registration form and handles the registration process
"""
class RegistrationView(generic.View):
    form_class = RegistrationForm # Specifying the form class to use 
    template_name = 'accounts/registration.html' # Specifying the location of your template

    # Function to execute upon receiving a GET request
    # This function is just for demonstration purpose and not necessary
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username') # Gets the username provided as a GET argument
        form = self.form_class(initial={'username' : username}) # Sets the initial value of the username field to the username from the GET argument

        context = {
            'form' : form,
        }

        return render(request, template_name=self.template_name, context=context) # Returns "accounts/registration.html" with provided context


    # Function to execute upon receiving a POST request
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST) # Gets the data from the POST request
        
        # Executes if the form passes all validators
        if form.is_valid():
            form.save() # Apply RegistrationForm's overriden save function note that by default the save function will save a model object 

        return render(request, self.template_name, {'form': form}) # Returns "accounts/registration.html" with the provided context in the 3rd argument

"""
Function-based view which presents the registration form and handles the registration process
"""
# def register(request):
#     # Handles the POST request
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST) # Gets the data from the POST request

#         # Check if the form is valid:
#         if form.is_valid():
#             form.save() # Apply RegistrationForm's overriden save function note that by default the save function will save a model object 
    
#     # Handles the GET request
#     else:
#         form = RegistrationForm(initial={'username': 'serge'})
    
#     context = {
#         'form' : form,
#     }
    
#     return render(request, 'accounts/registration.html', context) # Returns "accounts/registration.html" with provided context