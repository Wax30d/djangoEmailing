from django.shortcuts import render
from projectSendingEmail.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


# Create your views here.
# Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Wax30d Web'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject,
                  message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'proApp/success.html', {'recepient': recepient})
    return render(request, 'proApp/index.html', {'form': sub})
