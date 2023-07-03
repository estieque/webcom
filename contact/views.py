import json
from django.shortcuts import redirect, render
from contact.models import ContactMessage, ContactSeoSnippets, ContactSlider
from django.contrib import messages
from emaillist.models import EmailSubs
from homepage.models import SiteSetting

# Create your views here.
def contact(request):
    settings = SiteSetting.objects.all()
    cslider = ContactSlider.objects.all().order_by('-id')[:1]
    c_seo = ContactSeoSnippets.objects.all().order_by('-s_id')[:1]
    context={'settings':settings, 
             'cslider':cslider,  
             'c_seo':c_seo, }
    if request.method == "GET":
        return render(request, 'contact-us.html',context)
    elif request.method=="POST":
        if 'formone' in request.POST:
            name=request.POST.get('name')
            email=request.POST.get('email')
            number=request.POST.get('number')
            location=request.POST.get('location')
            message=request.POST.get('message')
            en=ContactMessage(name=name,email=email,message=message,number=number,location=location)
            en.save()
            messages.success(request, 'Votre message a été envoyé avec succès')
        if 'formtwo' in request.POST:
            emails=request.POST.get('emails')
            email=EmailSubs(emails=emails)
            email.save()
            messages.success(request, 'Merci de nous abonner')
        return render(request, 'contact-us.html',context)
    
    