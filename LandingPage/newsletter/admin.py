from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp

# Register your models here.


class SignUpAdmin(admin.ModelAdmin):
    list_display=["full_name" ,"subject","to"]
    form = SignUpForm

admin.site.register(SignUp,SignUpAdmin)