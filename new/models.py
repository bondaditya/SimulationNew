from decimal import Decimal
from django.conf import settings
from django.db.models.signals import pre_save, post_save, post_delete
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
# Create your models here.
#from courses.utils import create_slug

class VendorQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def unused(self):
        return self.filter(Q(lecture__isnull=True)&Q(category__isnull=True))


class VendorManager(models.Manager):
    def get_queryset(self):
        return VendorQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()

	
class Vendor(models.Model):
    #title           = models.CharField(max_length=120)
    #slug            = models.SlugField(blank=True)
    #embed_code      = models.TextField()
    #free            = models.BooleanField(default=True)
    member_required = models.BooleanField(default=False)
    #updated         = models.DateTimeField(auto_now=True)
    #timestamp       = models.DateTimeField(auto_now_add=True)
    #name_1 			= models.CharField(verbose_name='Name of the vendor 1', max_length=120,  default='Aacva')
   
    name 			= models.CharField(verbose_name='Name of the vendor 4', max_length=120,  default='Aada')
    description     = models.TextField(blank=True)
    cost_index 		= models.DecimalField(max_digits=50, blank = False, decimal_places=1, default=1)
    delivery_index  = models.DecimalField(max_digits=50, blank = False, decimal_places=1, default=1)
    quality_index 	= models.DecimalField(max_digits=50, blank=False, decimal_places=1, default=1)
    yearly_binding 	= models.BooleanField(default=False)
    delivery_time 	= models.IntegerField(default=30, blank=False, help_text = 'in days')
    unit_cost 		= models.IntegerField(verbose_name ='Cost per unit', default=500, blank=False)
    vendor_cost 	= models.DecimalField(max_digits=50, blank=False, decimal_places=2)
    tax_percentage  = models.DecimalField(max_digits=10, decimal_places=5, default=0.085)
    subtotal 		= models.DecimalField(max_digits=50, decimal_places=2, default=25.00)
    tax_total 		= models.DecimalField(max_digits=50, decimal_places=2, default=25.00)
    total 			= models.DecimalField(max_digits=50, decimal_places=2, default=25.00)
    monthly_order   = models.PositiveIntegerField(blank=False, default=500)

    


    objects = VendorManager()

    def __str__(self): 
        return self.name

    

    def vendor_cost(self):
    	uc = self.unit_cost
    	mo = self.monthly_order
    	vendor_cost = uc*mo 
    	self.vendor_cost = vendor_cost
    	return vendor_cost
    	

    def total(self):
        if self.yearly_binding == True:
           	return self.unit_cost*self.monthly_order*12
        else:
        	return self.unit_cost*self.monthly_order*3
         	

def tax_total_pre_save_receiver(sender, instance, *args, **kwargs):
	    total = instance.total() 
	    tax_percentage = instance.tax_percentage
	    tax_total = (total)*(1+(tax_percentage)) 
	    instance.tax_total = tax_total
        
pre_save.connect(tax_total_pre_save_receiver, sender= Vendor)

class DemandQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def unused(self):
        return self.filter(Q(lecture__isnull=True)&Q(category__isnull=True))


class VendorTotal(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

	def __str__(self):
		return self.vendor

class DemandManager(models.Manager):
    def get_queryset(self):
        return DemandQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()

class Demand(models.Model):
	employee_name_1   			= models.CharField(max_length=120, blank=False, default='aaaa')
	employee_name_2   			= models.CharField(max_length=120, blank=False, default='aaab')
	employee_name_3   			= models.CharField(max_length=120, blank=False, default='aaac')
	employee_name_4   			= models.CharField(max_length=120, blank=False, default='aaad')
	demand_1  		    			= models.PositiveIntegerField(blank=False, default=12000)
	demand_2  		    			= models.PositiveIntegerField(blank=False, default=12000)
	demand_3  		    			= models.PositiveIntegerField(blank=False, default=12000)
	demand_4  		    			= models.PositiveIntegerField(blank=False, default=12000)
	monthly_demand_1    	 	= models.PositiveIntegerField(blank=False, default=1000)
	monthly_demand_2    	 	= models.PositiveIntegerField(blank=False, default=1000)
	monthly_demand_3    	 	= models.PositiveIntegerField(blank=False, default=1000)
	monthly_demand_4    	 	= models.PositiveIntegerField(blank=False, default=1000)
	style_index_1   			    = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	style_index_2   			    = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	style_index_3   			    = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	style_index_4   			    = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	flavour_index_1 				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	flavour_index_2 				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	flavour_index_3 				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	flavour_index_4 				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	discount_index_1				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	discount_index_2				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	discount_index_3				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	discount_index_4				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	marketing_index_1				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	marketing_index_2				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	marketing_index_3				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	marketing_index_4				= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	new_style      				= models.BooleanField(default=False)
	new_flavour    				= models.BooleanField(default=False)
	discount       				= models.BooleanField(default=False)
	marketing      				= models.BooleanField(default=False)
	demand_value    			= models.PositiveIntegerField(blank=False, default=120000)
	monthly_demand_style_1 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_style_2 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_style_3 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_style_4 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_flavour_1 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_flavour_2 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_flavour_3 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_flavour_4 		= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_discount_1 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_discount_2 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_discount_3 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_discount_4 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_marketing_1 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_marketing_2 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_marketing_3 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_marketing_4 	= models.DecimalField(max_digits=5, decimal_places=1, default=1.00)
	monthly_demand_marketing_average 	= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_discount_average 	= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_style_average 	= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	monthly_demand_flavour_average 	= models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
	objects         			= DemandManager()

	def __str__(self):
		
			return self.employee_name_1


	def demand_1(self):
		return self.monthly_demand_1*12

	def demand_2(self):
		return self.monthly_demand_2*12

	def demand_3(self):
		return self.monthly_demand_3*12

	def demand_4(self):
		return self.monthly_demand_4*12 

	def monthly_demand_style_1(self):
		
			if self.new_style == True:
				monthly_demand_style_1 = self.monthly_demand_1*self.style_index_1
			else:
				monthly_demand_style_1 = self.monthly_demand_1
			self.monthly_demand_style_1 = monthly_demand_style_1
			return self.monthly_demand_style_1

	def monthly_demand_style_2(self):
		
			if self.new_style == True:
				monthly_demand_style_2 = self.monthly_demand_2*self.style_index_2
			else:
				monthly_demand_style_2 = self.monthly_demand_2
			self.monthly_demand_style_2 = monthly_demand_style_2
			return self.monthly_demand_style_2

	def monthly_demand_style_3(self):
		
			if self.new_style == True:
				monthly_demand_style_3 = self.monthly_demand_3*self.style_index_3
			else:
				monthly_demand_style_3 = self.monthly_demand_3
			self.monthly_demand_style_3 = monthly_demand_style_3
			return monthly_demand_style_3

	def monthly_demand_style_4(self):
		
			if self.new_style == True:
				monthly_demand_style_4 = self.monthly_demand_4*self.style_index_4
			else:
				monthly_demand_style_4 = self.monthly_demand_4
			self.monthly_demand_style_4 = monthly_demand_style_4
			return monthly_demand_style_4		


	def monthly_demand_flavour_1(self):
		
			if self.new_flavour == True:
				monthly_demand_flavour_1 = self.monthly_demand_1*self.flavour_index_1
			else:
				monthly_demand_flavour_1 = self.monthly_demand_1
			self.monthly_demand_flavour_1 = monthly_demand_flavour_1
			return monthly_demand_flavour_1

	def monthly_demand_flavour_2(self):
		
			if self.new_flavour == True:
				monthly_demand_flavour_2 = self.monthly_demand_2*self.flavour_index_2
			else:
				monthly_demand_flavour_2 = self.monthly_demand_2
			self.monthly_demand_flavour_2 = monthly_demand_flavour_2
			return monthly_demand_flavour_2

	def monthly_demand_flavour_3(self):
		
			if self.new_flavour == True:
				monthly_demand_flavour_3 = self.monthly_demand_3*self.flavour_index_3
			else:
				monthly_demand_flavour_3 = self.monthly_demand_3
			self.monthly_demand_flavour_3 = monthly_demand_flavour_3
			return monthly_demand_flavour_3

	def monthly_demand_flavour_4(self):
		
			if self.new_flavour == True:
				monthly_demand_flavour_4 = self.monthly_demand_4*self.flavour_index_4
			else:
				monthly_demand_flavour_4 = self.monthly_demand_4
			self.monthly_demand_flavour_4 = monthly_demand_flavour_4
			return monthly_demand_flavour_4


	def monthly_demand_discount_1(self):
		
			if self.discount == True:
				monthly_demand_discount_1 = self.monthly_demand_1*self.discount_index_1
			else:
				monthly_demand_discount_1 = self.monthly_demand_1
			self.monthly_demand_discount_1 = monthly_demand_discount_1
			return monthly_demand_discount_1	

	def monthly_demand_discount_2(self):
		
			if self.discount == True:
				monthly_demand_discount_2 = self.monthly_demand_2*self.discount_index_2
			else:
				monthly_demand_discount_2 = self.monthly_demand_2
			self.monthly_demand_discount_2 = monthly_demand_discount_2
			return monthly_demand_discount_2

	def monthly_demand_discount_3(self):
		
			if self.discount == True:
				monthly_demand_discount_3 = self.monthly_demand_3*self.discount_index_3
			else:
				monthly_demand_discount_3 = self.monthly_demand_3
			self.monthly_demand_discount_3 = monthly_demand_discount_3
			return monthly_demand_discount_3

	def monthly_demand_discount_4(self):
		
			if self.discount == True:
				monthly_demand_discount_4 = self.monthly_demand_4*self.discount_index_4
			else:
				monthly_demand_discount_4 = self.monthly_demand_4
			self.monthly_demand_discount_4 = monthly_demand_discount_4
			return monthly_demand_discount_4		

	

	def monthly_demand_marketing_1(self):
		
			if self.marketing == True:
				monthly_demand_marketing_1 = self.monthly_demand_1*self.marketing_index_1
			else:
				monthly_demand_marketing_1 = self.monthly_demand_1
			self.monthly_demand_marketing_1 = monthly_demand_marketing_1
			return self.monthly_demand_marketing_1

	def monthly_demand_marketing_2(self):
		
			if self.marketing == True:
				monthly_demand_marketing_2 = self.monthly_demand_2*self.marketing_index_2
			else:
				monthly_demand_marketing_2 = self.monthly_demand_2
			self.monthly_demand_marketing_2 = monthly_demand_marketing_2
			return monthly_demand_marketing_2

	def monthly_demand_marketing_3(self):
		
			if self.marketing == True:
				monthly_demand_marketing_3 = self.monthly_demand_3*self.marketing_index_3
			else:
				monthly_demand_marketing_3 = self.monthly_demand_3
			self.monthly_demand_marketing_3 = monthly_demand_marketing_3
			return monthly_demand_marketing_3

	def monthly_demand_marketing_4(self):
		
			if self.marketing == True:
				monthly_demand_marketing_4 = self.monthly_demand_4*self.marketing_index_4
			else:
				monthly_demand_marketing_4 = self.monthly_demand_4
			self.monthly_demand_marketing_4 = monthly_demand_marketing_4
			return monthly_demand_marketing_4


	def monthly_demand_style_average(self):

		    monthly_demand_style_average = (self.monthly_demand_style_1 
		    	+ Decimal(self.monthly_demand_style_2())+Decimal(self.monthly_demand_style_3())
		    	+Decimal(self.monthly_demand_style_4()))
		    self.monthly_demand_style_average = Decimal(monthly_demand_style_average)/4
		    return self.monthly_demand_style_average


	def monthly_demand_flavour_average(self):

		    monthly_demand_flavour_average = (Decimal(self.monthly_demand_flavour_1) 
		    	+ Decimal(self.monthly_demand_flavour_2())+Decimal(self.monthly_demand_flavour_3())
		    	+Decimal(self.monthly_demand_flavour_4()))
		    self.monthly_demand_flavour_average = Decimal(monthly_demand_flavour_average)/4
		    return self.monthly_demand_flavour_average	


	def monthly_demand_discount_average(self):
				monthly_demand_discount_average = (Decimal(self.monthly_demand_discount_1) 
			    	+ Decimal(self.monthly_demand_discount_2())+Decimal(self.monthly_demand_discount_3())
			    	+Decimal(self.monthly_demand_discount_4()))
				self.monthly_demand_discount_average = Decimal(monthly_demand_discount_average)/4
				return self.monthly_demand_discount_average
		    


	def monthly_demand_marketing_average(self):
				monthly_demand_marketing_average = self.monthly_demand_marketing_4+self.monthly_demand_marketing_3+self.monthly_demand_marketing_2+Decimal(self.monthly_demand_marketing_1())
				self.monthly_demand_marketing_average = Decimal(monthly_demand_marketing_average)/4
				return self.monthly_demand_marketing_average


class DemandForcast(models.Model):
		demand_title = models.CharField(max_length=120, blank=True)
		demand_forcast = models.PositiveIntegerField(blank=False, default=1000)
		total_cost = models.PositiveIntegerField(blank=False, default=12000)
		unit_cost = models.PositiveIntegerField(blank=False,default=1000)
		unit_price = models.PositiveIntegerField(blank=False, default=1500)
		unit_proft = models.PositiveIntegerField(blank=False, default=500)

		def __str__(self):
			return self.demand_title

		def total_cost(self):

			total_cost = self.demand_forcast*self.unit_cost
			self.total_cost = total_cost
			return self.total_cost

		def unit_profit(self):
			unit_profit=self.unit_price-self.unit_cost
			self.unit_profit = unit_profit
			return unit_profit

