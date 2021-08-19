from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from App_Login.forms import CreateNewUser,Login_form,EditProfile
from App_Login.models import UserProfile
from django.urls import reverse,reverse_lazy
from App_Posts.forms import PostForm


# Create your views here.
def sign_up(request):
    form=CreateNewUser()
    if request.method == 'POST':
        form=CreateNewUser(request.POST)
        if form.is_valid():
            user= form.save()
            user_profile=UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'App_Login/sign_up.html',context={'title':'Signup.YOUTUBE','form':form})

def login_page(request):
    form=Login_form()
    if request.method == 'POST':
        form=Login_form(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('main'))
    return render(request,'App_Login/login.html',context={'title':'Login','form':form})

@login_required
def edit_profile(request):
    current_user=UserProfile.objects.get(user=request.user)
    form=EditProfile(instance=current_user)
    if request.method=='POST':
        form=EditProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            form=EditProfile(instance=current_user)
            # app_login:profile
            return HttpResponseRedirect(reverse('main'))
    return render(request,'App_Login/edit_profile.html',context={'form':form})

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))

@login_required
def profile(request):
    form=PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
    return render(request,'App_Login/profile.html',context={'form':form})

@login_required
def profile_others(request,username):
    user_other=User.objects.get(username=username)
    if user_other==request.user:
        return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'App_Login/Profile_Search.html',context={'user_other':user_other,})

