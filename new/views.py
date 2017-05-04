from django.http import JsonResponse
from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import VendorForm, DemandForm, ForcastForm
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .models import Vendor, VendorTotal, Demand, DemandForcast 

User = get_user_model()




def IntroView(request):

    return render(request, "new/introduction.html")

def TeamView(request):
    return render(request,"new/team.html")

def DesignView(request):

    if request.method=="POST":
        form = DemandForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:design')
    else:
        form = DemandForm

    context = { 
    'demand': Demand.objects.all(),
    'form': form
    }
    return render(request, "new/design.html", context)    

def DesignUpdateView(request, id=None):
    instance = get_object_or_404(Demand, id=id)
    form = DemandForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return redirect('vendor:design')

    context = {
        "demand": Demand.objects.all(),
        "instance": instance,
        "form":form,
    }
    return render(request, "new/design_form.html", context)

def ProductionView(request):

    if request.method=="POST":
        form = ForcastForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:forcast')
    else:
        form = ForcastForm

    context = { 
    'demand': DemandForcast.objects.all(),
    'form': form
    }
    return render(request, "new/production.html", context)    

def ForcastUpdateView(request, id=None):
    instance = get_object_or_404(Demand, id=id)
    form = ForcastForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return redirect('vendor:production')

    context = {
        "demandforcast": DemandForcast.objects.all(),
        "vendor": Vendor.objects.all(),
        "demand" : Demand.objects.all(),

        "instance": instance,
        "form":form,
    }
    return render(request, "new/forcast_form.html", context)

def SupplyView(request):

    if request.method=="POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:supply')
    else:
        form = VendorForm

    context = { 
    'vendor': Vendor.objects.all(),
    'form': form
    }
    return render(request, "new/supply.html", context)    

def SupplyUpdateView(request, id=None):
    instance = get_object_or_404(Vendor, id=id)
    form = VendorForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return redirect('vendor:supply')

    context = {
        "vendor": Vendor.objects.all(),
        "demand": Demand.objects.all(),
        "instance": instance,
        "form":form,
    }
    return render(request, "new/supply_form.html", context)

def ResultView(request):

    if request.method=="POST":
        form = DemandForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:result')
    else:
        form = DemandForm

    context = { 
    'demand': Demand.objects.all(),
    'form': form
    }
    return render(request, "new/result.html", context)    

def ResultUpdateView(request, id=None):
    instance = get_object_or_404(Demand, id=id)
    form = DemandForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return redirect('vendor:result')

    context = {
        "demand": Demand.objects.all(),
        "instance": instance,
        "form":form,
    }
    return render(request, "new/result_form.html", context)

def BoardView(request):

    if request.method=="POST":
        form = DemandForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:board')
    else:
        form = DemandForm

    context = { 
    'demand': Demand.objects.all(),
    'form': DemandForm,
    }
    return render(request,'new/board.html',context)




