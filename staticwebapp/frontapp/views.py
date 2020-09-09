from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import UserForm
from .models import UserModel
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail


from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage, send_mail



# Create your views here.
def index(request):
    title ="Index"
    form = UserForm
    context={
        'title': title,
        'form': form,
    }
    return render(request, 'index.html', context )


def addemail(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # subject="welcome to site"
        # message= "Hope you are enjoying ecommerce"
        # recepient = "ronuresearch@gmail.com"
        # send_mail('test', 'content', settings.EMAIL_HOST_USER, ['ronuresearch@gmail.com'], fail_silently=False)
        # #send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        if form.is_valid():
            print(form.cleaned_data['user_email'])
            form.save()
            return HttpResponse('We got your email, Thank You')
        return render(request, 'index.html', {'form': form})