from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from App_Posts.models import Post
from django.contrib.auth.models import User

class Home(ListView):
    context_object_name='posts'
    model=Post
    template_name='App_Posts/home.html'

def home(request):
    posts=Post.objects.all()
    if request.method == 'GET':
        search=request.GET.get('search','')
        result=Post.objects.filter(caption__icontains=search)
        result1=Post.objects.exclude(pk__in=result).filter(catagory__icontains=search)
        
    return render(request,'App_Posts/home.html',context={'posts':posts,'search':search,'result':result,'result1':result1})