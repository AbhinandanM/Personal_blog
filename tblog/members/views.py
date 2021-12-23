from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.views.generic import  CreateView, UpdateView
from django.urls import reverse_lazy
from members.forms import SignUpForm, EditProfileForm




class UserRegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post-list')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('login')

#class PasswordsResetForms()




