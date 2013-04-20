from django.http import HttpResponse
from django.shortcuts import render
from home.models import *
from django.core.mail import send_mail
from django.core.context_processors import csrf
import datetime

def home(request):
    thanks = None
    if request.method == 'POST':
        # get email address, send email address to asorti@mit
        if 'email' in request.POST.keys():
            email = request.POST['email']
            currTime = datetime.datetime.now()
            beta_signup = BetaSignup(email=email, signed_up_on=currTime)
            beta_signup.save()
            send_mail('Asorti Signup', '%s' % email, 'asortistyle@gmail.com',['asorti@mit.edu'], fail_silently=False)
            thanks = True
    context = {'thanks' : thanks}
    context.update(csrf(request))
    return render(request, 'home/index.html', context)

def demo(request):
    return render(request, 'home/demo.html', {})