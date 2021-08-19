from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from App_Posts.models import Post,Likes
from App_Posts.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
@login_required
def upload(request):
    form=PostForm()
    if request.method == 'POST':
        print(request)
        form=PostForm(request.POST,request.FILES)
        # print('Form Post')
        # print(form['website'].value()=='' and form['video'].value()==None)
        # print('website')
        # print(form['website'].value()=='')
        # print('video')
        # print( form['video'].value()==None)
        if (form['website'].value()=='' and form['video'].value()==None ):
            # alert='Please fillup website or video field'
            messages.warning(request,'Please fillup website or video field')
            pass
        else :
            if (form['website'].value()!='' and form['video'].value()!=None ):
                # alert="You can't fill up website and video field together.Please link and video one by one"
                messages.info(request,"You can't fill up website and video field together.Please upload link and video one by one")
                pass
            else:
                if form.is_valid():
                    post=form.save(commit=False)
                    post.author=request.user
                    post.save()
                    return HttpResponseRedirect(reverse('main'))
    return render(request,'App_Posts/Upload.html',context={'form':form,})

@login_required
def edit_post(request,pk):
    post_info=Post.objects.get(pk=pk)
    form=PostForm(instance=post_info)
    if request.method == 'POST':
        #print(request)
        form=PostForm(request.POST,request.FILES,instance=post_info)
        # print('Form Post')
        # print(form['website'].value()=='' and form['video'].value()==None)
        # print('website')
        # print(form['website'].value()=='')
        # print('video')
        print( form['video'].value())
        print( form['website'].value())
        if (form['website'].value()=='' and (form['video'].value()==None or (not form['video'].value())) ):
            # alert='Please fillup website or video field'
            messages.warning(request,'Please fillup website or video field')
            pass
        else :
            if (form['website'].value()!='' and ( form['video'].value()==True)  ):
                # alert="You can't fill up website and video field together.Please link and video one by one"
                print('I am from 1')
                messages.info(request,"You can't fill up website and video field together.Please upload link and video one by one")
                pass
            else:
                #  if form.is_valid():
                #         post=form.save(commit=False)
                #         post.author=request.user
                #         post.save()
                #         return HttpResponseRedirect(reverse('main'))
                if (form['website'].value()!='' and ( form['video'].value()!='')  ):
                    print('I am from 2')
                    # alert="You can't fill up website and video field together.Please link and video one by one"
                    if (form['video'].value()):
                        messages.info(request,"You can't fill up website and video field together.Please upload link and video one by one")
                        pass
                    else:
                        if form.is_valid():
                            post=form.save(commit=False)
                            post.author=request.user
                            post.save()
                            return HttpResponseRedirect(reverse('main'))
                else:
                    if form.is_valid():
                        post=form.save(commit=False)
                        post.author=request.user
                        post.save()
                        return HttpResponseRedirect(reverse('main'))
    return render(request,'App_Posts/Upload.html',context={'form':form,})

# def edit_artist(request,pk):
#     post_info=Post.objects.get(pk=pk)
#     form=PostForm(instance=post_info)
#     if request.method == 'POST':
#         form=PostForm(request.POST,request.FILES,instance=post_info)
#         if (form['website'].value()=='' and form['video'].value()==None ):
#               # alert='Please fillup website or video field'
#              messages.warning(request,'Please fillup website or video field')
#             pass
#         else :
#             if (form['website'].value()!='' and form['video'].value()!=None ):
#             # alert="You can't fill up website and video field together.Please link and video one by one"
#                 messages.info(request,"You can't fill up website and video field together.Please upload link and video one by one")
#                 pass
#             else:
#             if form.is_valid():
#                 post=form.save(commit=False)
#                 post.author=request.user
#                 post.save()
#                 return HttpResponseRedirect(reverse('main'))
# return render(request,'App_Posts/Upload.html',context={'form':form,})
#         if form.is_valid():
#             form.save(commit=True)
#             return album_list(request,artist_id)
#     diction={'edit_form':form,'artist_id':artist_id}
#     return render(request,'first_app/edit_artist.html',context=diction)

class VideoDetails(DetailView):
    context_object_name='post'
    model=Post
    print(model)
    template_name='App_Posts/details.html'

def video(request,pk):
    post=Post.objects.get(pk=pk)
    other_post=Post.objects.exclude(pk=pk).filter(author=post.author)
    other_post1=Post.objects.exclude(pk=pk).filter(catagory__icontains=post.catagory)
    # print(post.author)
    other_post2=Post.objects.exclude(pk=pk).filter(caption__icontains=post.caption)
    other_post3=Post.objects.exclude(pk=pk).filter(pk__iregex='^\d*[02468]$')
    comment_form=CommentForm()
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user= request.user
            comment.post= post
            comment.save()
    return render(request,'App_Posts/details.html',context={'post':post,'other_post':other_post,'comment_form':comment_form,'other_post1':other_post1,'other_post2':other_post2,'other_post3':other_post3})

@login_required
def details_comment(request,pk):
    post=Post.objects.get(pk=pk)
    already_liked=Likes.objects.filter(post=post,user=request.user)
    if already_liked:
        liked=True
    else:
        liked=False
    comment_form=CommentForm()
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user= request.user
            comment.post= post
            comment.save()
            return HttpResponseRedirect(reverse('app_posts:details',kwargs={'pk':pk}))
    return render(request,'App_Posts/details.html',context={'post':post,'comment_form':comment_form,'liked':liked})

class Edit(LoginRequiredMixin,UpdateView):
    # context_object_name='post'
    model=Post
    fields=('video','website','caption','catagory','description',)
    template_name='App_Posts/edit_post.html'
    def get_success_url(self, **kwargs) :
        return reverse_lazy('app_post:details',kwargs={'pk':self.object.pk})

class DeletePost(LoginRequiredMixin,DeleteView):
    context_object_name='post'
    model=Post
    success_url=reverse_lazy('app_login:profile')
    template_name='App_Posts/delete_post.html'

@login_required
def user_video(request):
    posts=Post.objects.filter(author=request.user)
    return render(request,'App_Posts/user_video.html',context={'posts':posts})

class DeleteVideo(LoginRequiredMixin,DeleteView):
    context_object_name='post'
    model=Post
    success_url=reverse_lazy('app_post:user_video')
    template_name='App_Posts/delete_video.html'