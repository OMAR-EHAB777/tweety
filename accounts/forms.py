from django_registration.forms import RegistrationForm
from .models import customuser

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model=customuser