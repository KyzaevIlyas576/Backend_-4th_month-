from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)


class ResumeForm(UserCreationForm):
    email = forms.EmailField(required=True, initial='gmail.com')
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, initial="+996")
    gender = forms.ChoiceField(choices=GENDER, required=True, initial="М")


    class Meta:
        model = models.Resume
        fields = (
                'name',
                'surname',
                'age',
                'email',
                'photo',
                'resume',
                'phone_number',
                'gender',
                'address',
                'experience',
                'education',
                'skills'
        )

    def save(self, commit = True):
            user = super(ResumeForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()