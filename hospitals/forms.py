from django import forms
from django.contrib.auth.models import User
from .models import Doctor

class DoctorCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = ['name', 'mobile', 'special']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        doctor = super(DoctorCreationForm, self).save(commit=False)
        doctor.user = user
        if commit:
            doctor.save()
        return doctor
