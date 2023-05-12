from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.db.models import Count, Q
from django.shortcuts import render
from blog.models import BlogPost, PostAuthor
from emaillist.models import EmailSubs
from gallery.models import Gallery
from homepage.models import SiteSetting
from .models import BlogSeoSnippets, BlogSlider,Comments, PostCategory
from .views import *
# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    b_seo = BlogSeoSnippets.objects.all().order_by('-s_id')[:1]
    blogslider = BlogSlider.objects.all().order_by('-id')[:1]
    context = {'blogs':blogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider, 'homeblogs':homeblogs, 
               'b_seo':b_seo, }
    return render(request, 'blogs.html', context)




def blog_detail(request, slug_url):
    blogd = BlogPost.objects.get(slug=slug_url)
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    nextblogs = BlogPost.objects.all().order_by('add_date')[:1]
    prevblogs = BlogPost.objects.all().order_by('-add_date')[:1]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    pcat = PostCategory.objects.all()
    gallery = Gallery.objects.all().order_by('-id')[:9]
    blogslider = BlogSlider.objects.all().order_by('-id')[:1]
    comments = Comments.objects.all().filter(post = blogd)
    context ={'blogd':blogd,'homeblogs':homeblogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider,'comments':comments, 
              'nextblogs':nextblogs, 
              'prevblogs':prevblogs, 
              'pcat':pcat, 
              'gallery':gallery, 
              }
    if request.method == "GET":
        return render(request, 'blog-single.html',context)
    elif request.method=="POST":
        if 'formone' in request.POST:
            emails=request.POST.get('emails')
            email=EmailSubs(emails=emails)
            email.save()
            messages.success(request, 'Merci de nous abonner')
        if 'formtwo' in request.POST:
            name=request.POST.get('name')
            email=request.POST.get('emailadd')
            content=request.POST.get('content')
            cmnt=Comments(name=name,email=email,content=content,)
            cmnt.save()
            messages.success(request, 'Votre commentaire a été publié avec succès')
        return render(request, 'blog-single.html',context)

    
def read_category(request, slug_url):
    cats = PostCategory.objects.get(slug=slug_url)
    cblogs = BlogPost.objects.filter(PostCategory = cats)
    countcat = PostCategory.objects.annotate(num_blogs=Count('blog'))
    context={'cats':cats, 'cblogs': cblogs, 'countcat': countcat,}
    return render(request, 'category.html', context)


def blog_search(request):
    query = request.GET.get('q')
    sercblogs = BlogPost.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html', {'sercblogs': sercblogs})