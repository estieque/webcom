

from django.shortcuts import render, redirect
from contact.models import ContactMessage, ContactSeoSnippets, ContactSlider
from emaillist.models import EmailSubs
from homepage.models import SiteSetting
from django.contrib import messages
import requests

def contact(request):
    settings = SiteSetting.objects.all()
    cslider = ContactSlider.objects.all().order_by('-id')[:1]
    c_seo = ContactSeoSnippets.objects.all().order_by('-s_id')[:1]
    context = {
        'settings': settings,
        'cslider': cslider,
        'c_seo': c_seo,
    }

    if request.method == "GET":
        return render(request, 'contact-us.html', context)
    elif request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings[0].RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if result['success']:
            if 'formone' in request.POST:
                name = request.POST.get('name')
                email = request.POST.get('email')
                number = request.POST.get('number')
                location = request.POST.get('location')
                message = request.POST.get('message')
                contact_message = ContactMessage(name=name, email=email, message=message, number=number, location=location)
                contact_message.save()
                messages.success(request, 'Votre message a été envoyé avec succès')

            if 'formtwo' in request.POST:
                emails = request.POST.get('emails')
                email_subs = EmailSubs(emails=emails)
                email_subs.save()
                messages.success(request, 'Merci de nous abonner')

            return redirect('contact')  # Replace 'contact' with your actual URL name for the contact page
        else:
            messages.error(request, 'La vérification reCAPTCHA a échoué. Veuillez réessayer.')
            return redirect('contact')  # Replace 'contact' with your actual URL name for the contact page

    return render(request, 'contact-us.html', context)
