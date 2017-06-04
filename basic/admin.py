from django.contrib import admin

from .models import Marketing, Vendor, Demand, Costs
# Register your models here.


admin.site.register(Marketing)

admin.site.register(Vendor)

admin.site.register(Demand)


admin.site.register(Costs)