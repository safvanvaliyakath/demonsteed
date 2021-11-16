from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from . models import *
from django.contrib.auth.models import User,auth

# Create your views here.

def add(request):
    if request.method=='POST':
        nname=request.POST['nickname']
        desc=request.POST['role']
        img=request.FILES['img']
        s=listuser(name=nname,desc=desc,image=img)
        s.save()
        return redirect('/')
    return render(request,'addme.html')

class listview(ListView):
    model = listuser
    template_name = 'home.html'
    context_object_name = 'obj1'

class detailview(DetailView):
    model = listuser
    template_name = 'detail.html'
    context_object_name = 'obj2'

class updateview(UpdateView):
    model = listuser
    template_name = 'update.html'
    context_object_name = 'obj3'
    fields = ('name','desc','image')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = listuser
    template_name = 'delete.html'
    success_url = reverse_lazy('home')