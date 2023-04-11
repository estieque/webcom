from django.shortcuts import render
from gallery.models import Gallery, GallerySeoSnippets, GallerySlider

from homepage.models import SiteSetting

# Create your views here.
def gallery(request):
    settings = SiteSetting.objects.all()
    g_seo = GallerySeoSnippets.objects.all().order_by('-s_id')[:1]
    gallery = Gallery.objects.all()
    galslider = GallerySlider.objects.all().order_by('-id')[:1]
    context = {'settings':settings, 
               'g_seo':g_seo, 
               'gallery':gallery, 
               'galslider':galslider, 
               }
    return render(request, 'gallery.html', context)