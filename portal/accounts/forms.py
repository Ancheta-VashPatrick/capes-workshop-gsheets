from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model() # Gets custom user model

'''
Validator which checks if the username exists in the database
''' 
def validate_username(value):
    # Checks if username exists 
    if not(User.objects.filter(username=value).exists()):
        raise ValidationError(_('Username does not exist.'))

'''
Form for logging in
'''
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username:',
        validators=[validate_username],
        widget = forms.TextInput(attrs = {
            'class' : 'form-control w-100', # CSS class
        }),

    )
    
    password = forms.CharField(
        label='Password:',
        widget = forms.PasswordInput(attrs = {
            'class' : 'form-control w-100',
        }),
    )

    # This is just for demonstration purpose and does not have a function
    remember = forms.BooleanField(
        label='Remember me',
        required=False,
        widget = forms.CheckboxInput(attrs = {
            'class' : '',
        }),
    )

    # Validator for multiple fields which checks if the 'username' and 'password' fields are valid
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Checks if the username and password match
        if(not(authenticate(username=username, password=password))):
            raise forms.ValidationError(_('')) # This error message will not appear because it is not included in the template

'''
Form for registering
'''
class RegistrationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(render_value=True)) # Does not clear the 'password' field upon receiving a validation error
    # confirm_password = forms.CharField(widget=forms.PasswordInput(render_value=True)) # Does not clear the 'confirm_password' field upon receiving a validation error
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password'] # Only the required fields are included

    # Validator for the 'username' field
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Checks if username already exists
        if (User.objects.filter(username=username).exists()): 
            raise forms.ValidationError(_("Username already exists. :("))

        return username # We must return the validated field in order to have Django's default validators clean the field further

    # Validator for multiple fields which checks if the 'password' and 'confirm_password' fields are equal
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if (password != confirm_password):
            raise forms.ValidationError(_('Passwords do not match.'))

    # Overriding the default save function of the 'ModelForm' class since the default save function will not hash the password
    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        User.objects.create_user(username=username, password=password) # Creates a user with hashed password