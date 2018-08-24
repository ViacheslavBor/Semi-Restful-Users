from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
	context = {
	'user': User.objects.all(),
	}
	return render(request, 'file/allusers.html', context)

def new(request):
	return render(request, 'file/new.html')

def edit(request, id):
	user2 = User.objects.get(id=id)
	context = {
		'user': user2
	}
	return render(request, "file/edit.html", context)

def show(request, id):
	context={
		'user': User.objects.get(id=id)
	}
	return render(request, "file/show.html", context)

def create(request):
	user1 = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
	return redirect('/users/'+ str(user1.id))

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/users')

def update(request):
	if request.method == 'POST':
		b = User.objects.get(id = request.POST['user_id'])
		b.first_name = request.POST['first_name']
		b.last_name = request.POST['last_name']
		b.email = request.POST['email']
		b.save()
	return redirect('/users/'+ str(b.id))