from django.shortcuts import render, redirect
from .forms import SignUpForm
from . import forms
from django.contrib.auth import login
from . import models
from menu.models import List

def frontpage(request):
    books=models.Book.objects.all().order_by('-id')[:4]
    list=List.objects.all().order_by('-id')[:4]
    gimgs=models.EventsImage.objects.all().order_by('-id')[:5]
    return render(request, 'core/frontpage.html',{'books':books,'list':list,'gimgs': gimgs})
def book(request):
    books=models.Book.objects.all().order_by('-id')
    return render(request, 'core/book.html',{'books':books})



#show book details 
def book_detail(request, slug):

    post=models.Book.objects.get(slug=slug)


    if request.method == 'POST':
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.user = request.user
            obj.save()
        
            return redirect('book_detail', slug=post.slug)

    else:
        form=forms.CommentForm()
            

    return render(request, 'core/book_detail.html',{'book':post, 'form':form })


    
#eventsimage gallery
def eventsimage(request):
    gimgs=models.EventsImage.objects.all().order_by('-id')
    return render(request, 'core/gallery.html',{'gimgs':gimgs})   





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
