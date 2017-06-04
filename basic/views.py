from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Marketing, Vendor 
from .forms import SpentForm
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView
    )
#from allauth.accounts.views import SignupView, LoginForm

@login_required
def IntroView(request):
	
	
	context = {
		"name": 'user.username',
	}
	return render(request, "case/intro.html", context)


@login_required
class PlanningView(ListView):
	
	model= Vendor
	def get_queryset(self, arg):
		request = self.request
		qs=Vendor.objects.all()
		query = request.GET.get('q')
		if query:
			qs = qs.filter(name_icontains=query)
		return qs 
	form = SpentForm
	tenplate = 'case/planning.html'




@login_required
def SupplyView(request):
	
	#form = PostForm(request.POST or None, request.FILES or None)
	#if form.is_valid():
	#	instance = form.save(commit=False)
	#	instance.user = request.user
	#	instance.save()
	
	#messages.success(request, "Successfully Loggedin")
	#	return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"name": 'user.username',
	}
	return render(request, "case/supply.html", context)

@login_required
def MarketingView(request):
	
	#form = PostForm(request.POST or None, request.FILES or None)
	#if form.is_valid():
	#	instance = form.save(commit=False)
	#	instance.user = request.user
	#	instance.save()
	
	#messages.success(request, "Successfully Loggedin")
	#	return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"name": 'user.username',
	}
	return render(request, "case/marketing.html", context)

@login_required
def BudgetView(request):
	
	#form = PostForm(request.POST or None, request.FILES or None)
	#if form.is_valid():
	#	instance = form.save(commit=False)
	#	instance.user = request.user
	#	instance.save()
	
	#messages.success(request, "Successfully Loggedin")
	#	return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"name": 'user.username',
	}
	return render(request, "case/budget.html", context)

# Create your views here.
