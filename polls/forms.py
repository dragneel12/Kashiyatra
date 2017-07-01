from django import forms
from polls.models import *

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30 )
    last_name = forms.CharField(max_length=30)
    college_name=forms.CharField(max_length=100)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        userprofile = UserProfile.objects.create(user=user)
        userprofile.college_name = self.cleaned_data['college_name']
        userprofile.save()
