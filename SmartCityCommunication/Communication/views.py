from django.shortcuts import render
from .forms import *
from .models import Sender
from django.core.mail import send_mail
# Create your views here.

def sender(request):
    
    if request.method == 'POST':
        form = SenderForm(request.POST)
        if form.is_valid():
            form.save()
    form = SenderForm()
    
    return render(request, 'Communication/sender.html', {'form': form})

def addressee(request):
    data = Sender.objects.filter(wann__year=2020).order_by('-wann__day', 'grund')
    if request.method == 'POST':
        cust = Sender.objects.get(id=request.POST.get('custId'))
        subject = 'Antwort zu: '+cust.grund
        from_email = 'youremail@gmail.com'
        to_email = [cust.von]
        signup_message = request.POST.get('textfeld')   
        #Sendet eine EMail, funktioniert aber noch nicht, weil der Zielcomputer es nicht zulässt?
        send_mail(subject=subject, from_email = from_email, recipient_list=to_email, message=signup_message, fail_silently=True)
        cust.delete()
        data = Sender.objects.filter(wann__year=2020).order_by('wann', 'grund').reverse()
        return render(request, 'Communication/addressee.html',{'data':data})
    return render(request, 'Communication/addressee.html',{'data':data})

    

