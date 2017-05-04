from django.contrib import admin

from .models import Vendor, VendorTotal, Demand, DemandForcast


class VendorTotalInline(admin.TabularInline):
	model = VendorTotal

class VendorAdmin(admin.ModelAdmin):
	inlines = [
		VendorTotalInline
	]
	class Meta:
		model = Vendor




admin.site.register(Vendor, VendorAdmin)
admin.site.register(Demand)
admin.site.register(DemandForcast)
