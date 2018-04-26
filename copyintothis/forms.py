from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields=['full_name','email','subject','message','to']


    def clean_email(self):
        data = self.cleaned_data['email']
        #print(data)
        # if not ".edu" in data:
        #     raise forms.ValidationError("please use your school email !!")
        return data