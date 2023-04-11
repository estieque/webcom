from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from about.models import AboutContentOne, AboutContentTwo, AboutSeoSnippets, AboutSlider, ProgressBar

from homepage.models import SiteSetting, Slider
from portfolio.models import Portfolios, PortfolioCategory, PortfolioSeoSnippets, PortfolioSlider

# Create your views here.
def portfolio(request):
    settings = SiteSetting.objects.all()
    portfolio = Portfolios.objects.all()
    pslider = PortfolioSlider.objects.all().order_by('-id')[:1]
    pcat = PortfolioCategory.objects.all()
    p_seo = PortfolioSeoSnippets.objects.all().order_by('-s_id')[:1]
    context={'settings':settings, 'pslider':pslider, 'p_seo':p_seo, 'pcat':pcat, 'portfolio':portfolio,}
    return render(request, 'portfolio.html', context)




def port_detail(request, slug_url):
    portd = Portfolios.objects.get(slug=slug_url)
    portfolio = Portfolios.objects.all().order_by('-portfolio_id')[:3]
    #homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    settings = SiteSetting.objects.all()
    pslider = PortfolioSlider.objects.all().order_by('-id')[:1]
    context ={'portd':portd, 'settings':settings, 'pslider':pslider,'portfolio':portfolio,}
    return render(request, "portfolio-details.html", context)