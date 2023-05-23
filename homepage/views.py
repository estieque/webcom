from django.shortcuts import render
from about.models import AboutContentOne, AboutContentTwo
from blog.models import BlogPost

from homepage.models import SiteSetting, Slider
from portfolio.models import Portfolios
from scripts.models import FooterScript, HeaderScript
from services.models import Service
from team.models import TeamMember
from testimonial.models import Testimonial

# Create your views here.
def home(request):
    settings = SiteSetting.objects.all()
    h_slider = Slider.objects.all().order_by('-id')[:1]
    aboutone = AboutContentOne.objects.all().order_by('-content_id')[:1]
    portfolio = Portfolios.objects.all()
    testimonial = Testimonial.objects.all()
    abouttwo = AboutContentTwo.objects.all().order_by('-content_id')[:1]
    hscript = HeaderScript.objects.all().order_by('-s_id')[:1]
    fscript = FooterScript.objects.all().order_by('-s_id')[:1]
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    team = TeamMember.objects.all()
    service= Service.objects.all().order_by('-ser_id')[:4]
    hservice= Service.objects.all().order_by('ser_id')[:6]
    context={'settings':settings, 
             'h_slider':h_slider, 
             'aboutone':aboutone, 
             'portfolio':portfolio, 
             'testimonial':testimonial,
             'abouttwo':abouttwo, 
             'homeblogs':homeblogs, 
             'team':team, 
             'service':service, 
             'hservice':hservice, 
             'hscript':hscript,
             'fscript':fscript, 
             }
    return render(request, 'index.html', context)


def terms(request):
    settings = SiteSetting.objects.all()
    h_slider = Slider.objects.all().order_by('-id')[:1]
    aboutone = AboutContentOne.objects.all().order_by('-content_id')[:1]
    portfolio = Portfolios.objects.all()
    testimonial = Testimonial.objects.all()
    abouttwo = AboutContentTwo.objects.all().order_by('-content_id')[:1]
    hscript = HeaderScript.objects.all().order_by('-s_id')[:1]
    fscript = FooterScript.objects.all().order_by('-s_id')[:1]
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    team = TeamMember.objects.all()
    service= Service.objects.all().order_by('-ser_id')[:4]
    hservice= Service.objects.all().order_by('ser_id')[:6]
    context={'settings':settings, 
             'h_slider':h_slider, 
             'aboutone':aboutone, 
             'portfolio':portfolio, 
             'testimonial':testimonial,
             'abouttwo':abouttwo, 
             'homeblogs':homeblogs, 
             'team':team, 
             'service':service, 
             'hservice':hservice, 
             'hscript':hscript,
             'fscript':fscript, 
             }
    return render(request, 'terms.html', context)