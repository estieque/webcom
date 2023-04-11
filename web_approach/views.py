from django.shortcuts import render

from homepage.models import SiteSetting
from web_approach.models import FAQ, WebApproachContent, WebApproachSeoSnippets, WebApproachSlider

# Create your views here.
def webapproach(request):
    settings = SiteSetting.objects.all()
    apprslider = WebApproachSlider.objects.all().order_by('-id')[:1]
    approne = WebApproachContent.objects.all().order_by('-content_id')[:1]
    appr_seo = WebApproachSeoSnippets.objects.all().order_by('-s_id')[:1]
    faq = FAQ.objects.all()
    context={'settings':settings, 
             'apprslider':apprslider, 
             'approne':approne, 
             'appr_seo':appr_seo,
             'faq':faq, }
    return render(request, 'newapproaches.html', context)