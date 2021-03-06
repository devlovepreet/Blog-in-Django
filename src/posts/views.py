from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostForm
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save();
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	#if request.method == "POST":
		#print "title" + request.POST.get("title")
		#print request.POST.get("content")
		#Post.objects.create(title=title)
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id = None):
	#instance = Post.objects.get(id=3)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance" : instance
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title":"list"
	}
	#if request.user.is_authenticated():
	#	context ={
	#		"title":"My user list"
	#	}
	#else:
	#	context = {
	#		"title": "List"
	#	}
	return render(request,"post_list.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save();
		messages.success(request, "<a href='#''>Item</a> Saved",extra_tags = 'html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"title": instance.title,
		"instance" : instance,
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
	
