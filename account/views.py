# accounts/views.py
from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.urls import reverse_lazy
from django.views import generic


class GameUserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='First name')
    last_name = forms.CharField(required=True, label='Last name')
    email = forms.EmailField(
        required=True,
        label='Email',
        validators=[validate_email],
        error_messages={
            'exists': 'A user with this email already exists',
    })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = super(GameUserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SignUpView(generic.CreateView):
    form_class = GameUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
