from django.shortcuts import render,redirect
from .models import SJH
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def first(request):
    INFO = SJH.objects.all()
    # Paginator = Paginator(INFO,3)
    # now_page = request.GET.get('page')
    # INFO = Paginator.get_page(now_page)

    context ={
        "INFO" : INFO
    }

    return render(request,'first.html',context)

def readtext(request, post_id) :
    post = SJH.objects.get(id =post_id)
    context={
        "post":post
    }
    return render(request, 'readtext.html',context)

def createplace(request) :
    if request.method =="GET":

        return render(request,'createplace.html')
    elif request.method == "POST":
        post = SJH()
        post.user = request.user
        post.Name = request.POST['Name']
        post.Textarea = request.POST['Textarea']
        post.category = request.POST['category']
        try:
            post.pic = request.FILES['image']
        except:
            pass
        post.save()

        return redirect('first')


def update(request, post_id):
    if request.method =="GET":
        post = SJH.objects.get(id = post_id)
        context ={
            "post" : post,
        }

        return render(request,'update.html',context)
    elif request.method =="POST":
        post = SJH.objects.get(id = post_id)
        post.Name = request.POST['Name']
        post.Textarea = request.POST['Textarea']
        post.save()

        return redirect('first')

def delete(request,post_id):
    post = SJH.objects.get(id = post_id)
    post.delete()

    return redirect('first')

def deleteall(request):
    post = SJH.objects.all()
    post.delete()
    return redirect('first')

def search(request):
    search_Name = request.GET['search']
    search_filter = request.GET['search_filter']
    if search_filter == "제목1":
        posts = SJH.objects.filter(Name__icontains=search_Name)
    elif search_filter == "내용":
        posts = SJH.objects.filter(Textarea__icontains=search_Name)
    elif search_filter == "제목_내용    ":
        posts = SJH.objects.filter(Q(Name__icontains=search_Name)|Q(Textarea__icontains=search_Name))

    context={
        "posts":posts,
    }
    return render(request,'search.html',context)

def category(request):
    search_category = request.GET['category']
    post = SJH.objects.filter(category=search_category)
    context={
        "post":post
    }
    return render(request,'category.html',context)