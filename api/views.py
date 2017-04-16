import os
from django.shortcuts import render,redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from models import Document
from forms import DocumentForm
from django.conf import settings
MEDIA_ROOT = getattr(settings, "MEDIA_ROOT", None)

def index(request):
    return HttpResponse("Hello World")

def generate_key(request):
    from random import randint
    x= str(randint(234568, 984758))
    while os.path.exists(os.path.join(MEDIA_ROOT,x)):
        x= randint(234568, 984758)
    os.makedirs(os.path.join(MEDIA_ROOT,x))
    return HttpResponse(x)

def upload(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            api_key = data['apikey']
            if not os.path.exists(os.path.join(MEDIA_ROOT,api_key)):
                return HttpResponse("Invalid api key.")
            doc = request.FILES['image']
            from django.core.exceptions import ValidationError
            if not doc.content_type.startswith('image'):
                return HttpResponse('Unsupported file extension.')
            newdoc = Document(path = api_key, image = doc)
            newdoc.save()
            return redirect(reverse('upload'))
    return render(request,'upload.html',{ 'form': form})

def list_all(request,apikey):
    form = DocumentForm()
    documents = Document.objects.filter(path=apikey).all()
    return render(request,'list.html',{'documents': documents, 'form': form})

def detail(request,apikey,pk):
    form = DocumentForm()
    documents = Document.objects.filter(pk=pk)
    return render(request,'detail.html',{'documents': documents, 'form': form})

def delete(request,apikey,pk):
    form = DocumentForm()
    document =  get_object_or_404(Document,pk=pk)
    if os.path.exists(os.path.join(MEDIA_ROOT,document.image.name)):
        os.remove(os.path.join(MEDIA_ROOT,document.image.name))
    document.delete()
    return redirect('list_all',apikey=apikey)
