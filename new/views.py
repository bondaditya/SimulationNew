from django.http import JsonResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User, Group 
from invitations.models import Invitation
from invitations.forms import InviteForm
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, FormView


from .forms import VendorForm, ProductForm, ForcastForm, ProfileForm, VendorForm2, VendorForm3, VendorForm4
from .models import Vendor, Demand, Forcast, Product, Vendor2, Vendor3, Vendor4

User = get_user_model()



@login_required
def IntroView(request):
    context = {
    'demand': Demand.objects.filter().first(),
    'product': Product.objects.filter().first(),
    'forcast': Forcast.objects.all(),
    'users': User.objects.all(),
    'vendor':Vendor.objects.filter().first(),
    }
    return render(request, "new/introduction.html", context)

@login_required
def TeamView(request):

    return render(request,"new/team.html")



@login_required
def ProductView(request):

    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('vendor:design')
    else:
        form = ProductForm

    context = {
    'demand': Demand.objects.all(),
    'mo1': Demand.objects.get(id=1).monthly_forcast,
    'mo2': Demand.objects.get(id=2).monthly_forcast,
    'mo3': Demand.objects.get(id=3).monthly_forcast,
    'mo4': Demand.objects.get(id=4).monthly_forcast,
    'mo5': Demand.objects.get(id=4).monthly_forcast,
    'e1': Demand.objects.get(id=1).employee_name,
    'e2': Demand.objects.get(id=2).employee_name,
    'e3': Demand.objects.get(id=3).employee_name,
    'e4': Demand.objects.get(id=4).employee_name,
    'e5': Demand.objects.get(id=4).employee_name,
    'product':Product.objects.filter(user=request.user).first(),
    
    'form': form
    }
    return render(request, "new/design.html", context)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:design')



@login_required
def ProductionView(request):    
    return render(request, "new/production.html")

@login_required
def VendorCreateView(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('vendor:production')
    else:
        VendorForm  
    context = {
        "vendor": Vendor.objects.all(),
        "demand": Demand.objects.all(),
        'product': Product.objects.all(),
        
        "form":form,
    }
    return render(request, "new/vendor_form.html", context)  


class ForcastCreateView(LoginRequiredMixin, UpdateView):
    form_class = ForcastForm
    model = Forcast
    
      

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ForcastCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['vendor'] = Vendor.objects.filter(user=self.request.user).first(),
        context['demand'] = Demand.objects.all()
        context['product'] = Product.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:production')
        

@login_required
def SupplyView(request):
    context = {
    'vendor': Vendor.objects.filter(user=request.user).first(),
    'vendor2': Vendor2.objects.filter(user=request.user).first(),
    'vendor3': Vendor3.objects.filter(user=request.user).first(),
    'vendor4': Vendor4.objects.filter(user=request.user).first(),
    'forcast': Forcast.objects.get(user=request.user),
    'product': Product.objects.filter(user=request.user).first(),

    }
    return render(request, "new/supply.html", context)

@login_required
def SupplyCreateView(request):

    form = VendorForm()
    if request.method == 'POST':
    
        form = VendorForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('vendor:supply'))    
        else:
            form = VendorForm

    context = {
        "demand": Demand.objects.all(),
        "form":form,
        "vendor": Vendor.objects.all(),

    }
    return render(request, "new/supply_form.html", context)

@login_required
def ResultView(request):
    return render(request,"new/result.html")    


class SupplyUpdateView(LoginRequiredMixin, UpdateView):
    form_class = VendorForm
    model = Vendor 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:supply')

class SupplyUpdateView2(LoginRequiredMixin, UpdateView):
    form_class = VendorForm2
    model = Vendor2 


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:supply')

class SupplyUpdateView3(LoginRequiredMixin, UpdateView):
    form_class = VendorForm3
    model = Vendor3 
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:supply')

class SupplyUpdateView4(LoginRequiredMixin, UpdateView):
    form_class = VendorForm4
    model = Vendor4 
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:supply')




@login_required
def BoardView(request):
    context = {
    'demand': Demand.objects.filter().first(),
    'product': Product.objects.filter().first(),
    'forcast': Forcast.objects.all(),
    'users': User.objects.all(),
    'vendor':Vendor.objects.filter().first(),
    }

    return render(request,'new/board.html',context)

@login_required
def ReportView(request):
    context = {
    'demand': Demand.objects.filter().first(),
    'product': Product.objects.filter().first(),
    'forcast': Forcast.objects.all(),
    'users': User.objects.all(),
    'vendor':Vendor.objects.filter().first(),
    }

    return render(request,'new/report.html',context)


@login_required
def TestView(request):
    context = {
    
    'invitees':Invitation.objects.filter(inviter_id=request.user.id),
    'invitations': Invitation.objects.all(),
    'accepted':Invitation.objects.filter(inviter_id=request.user.id).filter(accepted=True),
    'inviteescount':Invitation.objects.filter(inviter_id=request.user.id).count(),
    'notaccepted':Invitation.objects.filter(inviter_id=request.user.id).filter(accepted=False)

    }

    return render(request, "new/test.html", context)




class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = User

    def get_initial(self):
        initial = super(UserProfileUpdateView, self).get_initial()
        try:
            current_group = self.object.groups.get()
        except:
            # exception can occur if the edited user has no groups
            # or has more than one group
            pass
        else:
            initial['group'] = current_group.pk
        return initial
        

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('vendor:intro')

    
class SendInvite(LoginRequiredMixin, FormView):
    template_name = 'invitations/forms/_invite.html'
    form_class = InviteForm

    
    def dispatch(self, request, *args, **kwargs):
        return super(SendInvite, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        try:
            invite = form.save(email)
            invite.inviter = self.request.user
            invite.save()
            invite.send_invitation(self.request)
        except Exception:
            return self.form_invalid(form)

        return self.render_to_response(
            self.get_context_data(
                success_message='%s has been invited' % email))

    context ={ 
    
    }

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), context)






    


# def GroupCreateView(request):
    
#     form = ProfileForm()
#     if request.method == 'POST':
#         form = ProfileForm(request.POST or None)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user 
#             instance.save()
#             return redirect('vendor:intro')    
#         else:
#             form = ProfileForm

#     if request.user.profile.type_user=='t':
#         g = Group.objects.get(name='Teacher') 
#         g.user_set.add(request.user)        

           
    
#     context = {
        
#         "form":form,
#     }
#     return render(request, "new/profile_form.html", context)

# class UserProfileUpdateView(UpdateView):
#     model = User

    
      
    
    
#     def get_initial(self):
#         initial = super(UserProfileUpdateView, self).get_initial()
#         try:
#             current_group = self.object.groups.get()
#         except:
#             # exception can occur if the edited user has no groups
#             # or has more than one group
#             pass
#         else:
#             initial['group'] = current_group.pk
#         return initial
        

    
#     def get_form_class(self):
#         return ProfileForm

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
    
#     def form_valid(self, form):
#         self.object.groups.clear()
#         self.object.groups.add(form.cleaned_data['group'])
#         return redirect('vendor:intro') 