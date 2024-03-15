from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm, SetPasswordForm)
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Адреса електронної пошти'
                                                           })
                             )
    first_name = forms.CharField(label="",
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': "Ім'я"
                                                               }))
    last_name = forms.CharField(label="",
                                max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Прізвище'
                                                              }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Нікнейм користувача'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ('<span class="form-text text-muted">'
                                             '<small>Може містити тільки до 150 знаків та символи @/./+/-/_.</small>'
                                             '</span>'
                                             )

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ('<ul class="form-text text-muted small">'
                                              '<li>Ваш пароль не повинен бути схожим з Вашими даними.</li>'
                                              '<li>Пароль має містити щонайменше 8 символів</li>'
                                              '<li>Ваш пароль має бути унікальним</li>'
                                              '<li>Пароль не може бути повністю чисельним.</li>'
                                              '</ul>'
                                              )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Підтвердження пароля'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ('<span class="form-text text-muted">'
                                              '<small>Введіть Ваш пароль повторно для верифікації.</small>'
                                              '</span>'
                                              )


class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Адреса електронної пошти'
                                                                     }
                                                              ))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                         'placeholder': "Ім'я"
                                                                                         }
                                                                                  ))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                        'placeholder': 'Прізвище'
                                                                                        }
                                                                                 ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Нікнейм користувача'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ('<span class="form-text text-muted">'
                                             '<small>Може містити тільки до 150 знаків та символи @/./+/-/_.</small>'
                                             '</span>'
                                             )


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        required=False)
    address1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адреса 1'}),
        required=False)
    address2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адреса 2'}),
        required=False)
    country = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Країна'}),
        required=False)
    city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Місто'}),
        required=False)
    state = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Область'}),
        required=False)
    zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поштовий індекс'}),
        required=False)

    class Meta:
        model = Profile
        fields = ('address1', 'address2', 'phone', 'city', 'state', 'zipcode')


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Новий пароль'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = ('<ul class="form-text text-muted small">'
                                                  '<li>Ваш пароль не повинен бути схожим з Вашими даними.</li>'
                                                  '<li>Пароль має містити щонайменше 8 символів</li>'
                                                  '<li>Ваш пароль має бути унікальним</li>'
                                                  '<li>Пароль не може бути повністю чисельним.</li>'
                                                  '</ul>'
                                                  )

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Підтвердження нового пароля'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = ('<span class="form-text text-muted">'
                                                  '<small>Введіть Ваш пароль повторно для верифікації.</small>'
                                                  '</span>'
                                                  )
