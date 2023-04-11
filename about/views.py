
from django.shortcuts import render
from about.models import AboutContentOne, AboutContentTwo, AboutSeoSnippets, AboutSlider, ProgressBar

from homepage.models import SiteSetting
from portfolio.models import Portfolios
from team.models import TeamMember
from testimonial.models import Testimonial

# Create your views here.
def about(request):
    settings = SiteSetting.objects.all()
    aslider = AboutSlider.objects.all().order_by('-id')[:1]
    aboutone = AboutContentOne.objects.all().order_by('-content_id')[:1]
    abouttwo = AboutContentTwo.objects.all().order_by('-content_id')[:1]
    progressbar = ProgressBar.objects.all().order_by('-progress_id')[:3]
    testimonial = Testimonial.objects.all()
    portfolio = Portfolios.objects.all().order_by('-portfolio_id')[:3]
    a_seo = AboutSeoSnippets.objects.all().order_by('-s_id')[:1]
    team = TeamMember.objects.all()
    context={'settings':settings, 
             'aslider':aslider, 
             'aboutone':aboutone, 
             'abouttwo':abouttwo, 
             'progressbar':progressbar, 
             'a_seo':a_seo, 
             'testimonial':testimonial,
             'portfolio':portfolio, 
             'team':team, }
    return render(request, 'about.html', context)