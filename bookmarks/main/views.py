from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


from main.models import Link
from main.models import Tag

# Create your views here.



def index(request):
    context = RequestContext(request)
    
    links = Link.objects.all()
    
    return render_to_response('main/index.html', {'links':links}, context)


def tags(request):
    context = RequestContext(request)

    tags = Tag.objects.all()

    return render_to_response('main/tags.html', {'tags':tags}, context)


def tag(request, tag_name):
    context = RequestContext(request)
    
    the_tag = Tag.objects.get(name=tag_name)
    links = the_tag.link_set.all()
    
    return render_to_response('main/index.html', {'links':links, 'tag_name': the_tag}, context)


def add_link(request):
    
    #context = RequestContext(request)
    try:
        if request.method == 'POST':
            url = request.POST.get("url","")
            tags = request.POST.get("tags","")
            title = request.POST.get("title","")

            l = Link.objects.get_or_create(title=title, url=url)[0]

            for atag in tags.split():
                t = Tag.objects.get_or_create(name=atag)[0]
                l.tags.add(t)
    except:
            return redirect(index)

    

    return redirect(index)
