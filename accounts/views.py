from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = "form.html"
    success_url = "/polls/"
