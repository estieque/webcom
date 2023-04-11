from django.shortcuts import render
from about.models import AboutSlider

from homepage.models import SiteSetting
from portfolio.models import Portfolios
from services.models import Service, ServiceSeoSnippets, ServiceSlider
from team.models import TeamMember

# Create your views here.
def service(request):
    settings = SiteSetting.objects.all()
    aslider = AboutSlider.objects.all().order_by('-id')[:1]
    portfolio = Portfolios.objects.all().order_by('-portfolio_id')[:3]
    ser_seo = ServiceSeoSnippets.objects.all().order_by('-s_id')[:1]
    team = TeamMember.objects.all()
    serslider = ServiceSlider.objects.all().order_by('-id')[:1]
    service = Service.objects.all()
    context={'settings':settings, 
             'aslider':aslider, 
             'ser_seo':ser_seo,
             'portfolio':portfolio, 
             'team':team, 
             'serslider':serslider, 
             'service':service, }
    return render(request, 'services.html', context)