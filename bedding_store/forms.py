from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
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
