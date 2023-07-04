from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first(request):
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pass']
        print(username)
        print(password)
        FO=Form.objects.get_or_create(username=username,password=password)[0]
        FO.save()
        return HttpResponse('data is inserted is successfully')
        
    return render(request,'first.html')

def insert_topic(request):
    if request.method=='POST':
        topic_name=request.POST['topic']
        print(topic_name)
        TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
        TO.save()
        return HttpResponse('data is inserted is successfully')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        topic_name=request.POST['tn']
        name=request.POST['na']
        url=request.POST['url']
        #print(topic_name)
        TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('data is inserted is successfully')

    return render(request,'insert_webpage.html')
def insert_access(request):
    if request.method=='POST':
        name=request.POST['na']
        date=request.POST['dt'] 
        author=request.POST['at']  
        WO=Webpage.objects.get(name=name)
        WO.save()     
        AO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()
        return HttpResponse('data is inserted is successfully')

    return render(request,'insert_access.html')
def insert_web_sel(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=="POST":
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST.get('url')
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url)[0]
        WO.save()
        return HttpResponse('webpage data is inserted')
    return render(request,'insert_web_sel.html',d)

def retrive_web(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
            
        RWST=request.POST.getlist('top')
        wos=Webpage.objects.none()
        for i in RWST:
            wos=wos| Webpage.objects.filter(topic_name=i)
        d1={'wos':wos}
        return render(request,'display_retrie.html',d1)

    return render(request,'retrive_web.html',d)
def web_radio(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'web_radio.html',d)