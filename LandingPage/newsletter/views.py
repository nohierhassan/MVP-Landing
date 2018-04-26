from django.shortcuts import render
from .models import SignUp
from .forms import SignUpForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        template = "newsletter/home.html"
    else:
        template = "registration/login.html"
    context={}

    form=SignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)  # to skip saving right away and do other stuff :)
        print(instance.email)
        subject=instance.subject
        message=instance.message
        to=instance.to
        instance.save()
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )


    if request.user.is_authenticated and request.user.is_staff:
        for i in SignUp.objects.all():
            print(i.full_name)
        queryset=SignUp.objects.all().order_by('-timestamp')
        context={

            "queryset":queryset
        }

    return render(request,template,context)




def about(request):
    return render(request,"newsletter/about.html",{})






def contact(request):
    if request.user.is_authenticated():
        template = "newsletter/contact.html"
    else:
        template = "newsletter/home_not_auth.html"

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)  # to skip saving right away and do other stuff :)
        print(instance.email)
        subject = instance.subject
        message = instance.message
        to = instance.to
        instance.save()
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )
    title="Contact Us"
    context = {
        "form": form,
        "title":title,
    }
    return render(request,"newsletter/contact.html",context)
