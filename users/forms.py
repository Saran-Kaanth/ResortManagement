# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms
from django.forms import TextInput, EmailInput,NumberInput,PasswordInput,RadioSelect    

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ("email",)


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ("email",)

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','password','first_name','last_name','age','gender','flat_no','area','city','state','pincode')
        
        gender_choices=(('Male','Male'),
                    ('Female','Female'),
                    ('Not Defined','Not Defined'))
        
        widgets = {
            'email':EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password':PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'age': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Age'
                }),
            'flat_no': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Flat no'
                }),
            'area': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Area'
                }),
            'city': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'City'
                }),
            'state': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'State'
                }),
            'pincode': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Pincode'
                }),
            
            # 'gender':RadioSelect(attrs={
            #     'class': "form-control", 
            #     'style': 'max-width: 300px;color:red',
            #     'placeholder': 'Last Name'
            # },choices=gender_choices)
        }
        
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=('email','password',)
        widgets = {
         'password':PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                # 'placeholder': 'Password'
                }),
        }
        name="saran"

class CustomStaffCreationForm(CustomUserCreationForm):
    class Meta:
        model=CustomUser
        fields=CustomUserCreationForm.Meta.fields+("is_staff",)
        gender_choices=CustomUserCreationForm.Meta.gender_choices
        widgets=CustomUserCreationForm.Meta.widgets

    def save(self):
        # print(self.cleaned_data)
        # print(super(UserLoginForm).name)
        CustomUser.objects.create_staff(email=self.cleaned_data['email'],password=self.cleaned_data['password'],first_name=self.cleaned_data['first_name'])
        print('success')
        # pass