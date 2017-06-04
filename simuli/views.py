from django.views.generic import ListView

from django.shortcuts import render

from django.shortcuts import render 



class HomeView(ListView):
    def get(self, request, *args, **kwargs): # GET -- retrieve view / list view / search


        context = {
            #"qs": qs,
            #"rec_courses": rec_courses,
            "name": 'user.username',

        }
        return render(request, "home.html", context)