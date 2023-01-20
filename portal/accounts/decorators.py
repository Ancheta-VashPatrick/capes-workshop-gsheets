from django.contrib.auth.decorators import user_passes_test

"""
Custom decorator to check if user has the 'is_company' field set to true
"""
def company_required(function):
    return user_passes_test(lambda user: user.is_company)(function)