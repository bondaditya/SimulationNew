import random
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q, Case, Value, When
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from annoying.fields import AutoOneToOneField

TITLE_CHOICES = (
    ('Jan', 'Jan'),
    ('Feb', 'Feb'),
    ('Mar', 'Mar'),
    ('Apr', 'Apr'),
    ('May', 'May'),
    ('Jun', 'Jun'),
    ('Jul', 'Jul'),
    ('Aug', 'Aug'),
    ('Sep', 'Sep'),
    ('Oct', 'Oct'),
    ('Nov', 'Nov'),
    ('Dec', 'Dec'),
)

DESIGN_CHOICES = (('style', 'Style'),('design','Design'),('discount','Discount'),('marketing','Marketing'))
# Create your models here.
#from courses.utils import create_slug


class College(models.Model):
    
    user = models.OneToOneField(User, related_name='college')
    college_name = models.CharField(max_length=20, default='IIM-A')

    def __str__(self):
        return 'College of user: {}'.format(self.user.username)

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





class DemandQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def unused(self):
        return self.filter(Q(lecture__isnull=True)&Q(category__isnull=True))




class DemandManager(models.Manager):
    def get_queryset(self):
        return DemandQuerySet(self.model, using=self._db)




class Demand(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL)
        employee_name = models.CharField(max_length=120, blank=False, default = 'Aditya')
        monthly_forcast = models.PositiveIntegerField(default=1000, blank = False)
        monthly_forcast_update = models.PositiveIntegerField(default=1000, blank = False)
        objects = DemandManager()

        def __str__(self): 
            return self.employee_name

class Product(models.Model):
        user = AutoOneToOneField(User, primary_key=True)
        
        style = models.BooleanField(default=False)
        storage = models.BooleanField(default=False)
        extended_battery = models.BooleanField(default=False)
        durability = models.BooleanField(default=False)
        unit_cost =  models.PositiveIntegerField(blank=False,default=130)
        unit_price =  models.PositiveIntegerField(blank=False,default=200)
        
        inventory_cost = models.PositiveIntegerField(blank=False,default=4)

        def __str__(self):
            return self.user.username

        @property
        def markdown_price(self):
            if self.style == True | self.storage==True| self.durability==True| self.extended_battery==True:
                return 113
            else:
                return 98       



class Forcast(models.Model):
        user = AutoOneToOneField(User, primary_key=True)
        forcast = models.PositiveIntegerField(blank=False,default=60)
        
        def __str__(self):
            return self.user.username

class Vendor(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    
    
    monthly_order1   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order2   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order3   = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Max Value is 25")
    start_month1     = models.CharField(max_length=3, choices=TITLE_CHOICES, default="Jan")
    start_month2     = models.CharField(max_length=3, choices=TITLE_CHOICES, default="Jan")
    start_month3     = models.CharField(max_length=3, choices=TITLE_CHOICES, default="Jan")
    created_at = models.DateTimeField(auto_now=True)
    mod_count = models.IntegerField(default=0)
    objects         = VendorManager()

    def save(self):
        self.mod_count +=1
        return super(Vendor,self).save()


    def __str__(self):
        return self.user.username
    @property
    def monthly_demand1(self):
        return self.monthly_order1+self.monthly_order2+self.monthly_order3

    @property
    def actual_demand1(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand1)*.8+.01*(self.monthly_demand1)
        else:
            return (self.monthly_demand1)*.8+.06*(self.monthly_demand1)

    @property
    def actual_demand2(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand1)*.8+.01*(self.monthly_demand1)
        else:
            return (self.monthly_demand1)*.8+.06*(self.monthly_demand1)
            
    @property
    def actual_demand3(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand1)*.8+.01*(self.monthly_demand1)
        else:
            return (self.monthly_demand1)*.8+.06*(self.monthly_demand1)

    @property
    def inventory1(self):
        return self.monthly_demand1-self.actual_demand1
    @property
    def inventory2(self):
        return self.monthly_demand1-self.actual_demand2
    @property
    def inventory3(self):
        return self.monthly_demand1-self.actual_demand3

class Vendor2(models.Model):
    user = AutoOneToOneField(User, primary_key=True) 
    monthly_order4   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order5   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order6   = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Max Value is 25") 
    created_at = models.DateTimeField(auto_now=True)
    mod_count = models.IntegerField(default=0)  
    def __str__(self):
        return self.user.username
    def save(self):
        self.monthly_demand4 = self.user.vendor.monthly_order1
        self.monthly_demand5 = self.user.vendor.monthly_order2
        self.monthly_demand6 = self.user.vendor.monthly_order3
        self.mod_count +=1
        super(Vendor2, self).save()
    @property
    def monthly_demand2(self):
        return self.monthly_order4+self.monthly_order5+self.monthly_order6

    @property
    def actual_demand4(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand2)*.8+.01*(self.monthly_demand2)
        else:
            return (self.monthly_demand2)*.8+.06*(self.monthly_demand2)
    @property
    def actual_demand5(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand2)*.8+.01*(self.monthly_demand2)
        else:
            return (self.monthly_demand2)*.8+.06*(self.monthly_demand2)
    @property
    def actual_demand6(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand2)*.8+.01*(self.monthly_demand2)
        else:
            return (self.monthly_demand2)*.8+.06*(self.monthly_demand2)
    @property
    def inventory4(self):
        return self.monthly_demand2-self.actual_demand4
    @property
    def inventory5(self):
        return self.monthly_demand2-self.actual_demand5
    @property
    def inventory6(self):
        return self.monthly_demand2-self.actual_demand6

class Vendor3(models.Model):
    user = AutoOneToOneField(User, primary_key=True) 
    monthly_order7   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order8   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order9   = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Max Value is 25")   
    created_at = models.DateTimeField(auto_now=True)
    mod_count = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
    def save(self):
        self.monthly_demand7 = self.user.vendor.monthly_order1
        self.monthly_demand8 = self.user.vendor.monthly_order2
        self.monthly_demand9 = self.user.vendor.monthly_order3
        self.mod_count +=1
        super(Vendor3, self).save()

    @property
    def monthly_demand3(self):
        return self.monthly_order7+self.monthly_order8+self.monthly_order9

    @property
    def actual_demand7(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand3)*.8+.01*(self.monthly_demand3)
        else:
            return (self.monthly_demand3)*.8+.06*(self.monthly_demand3)
    @property
    def actual_demand8(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand3)*.8+.01*(self.monthly_demand3)
        else:
            return (self.monthly_demand3)*.8+.06*(self.monthly_demand3)
    @property
    def actual_demand9(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand3)*.8+.01*(self.monthly_demand3)
        else:
            return (self.monthly_demand3)*.8+.06*(self.monthly_demand3)    
    @property
    def inventory7(self):
        return self.monthly_demand3-self.actual_demand7
    @property
    def inventory8(self):
        return self.monthly_demand3-self.actual_demand8
    @property
    def inventory9(self):
        return self.monthly_demand3-self.actual_demand9

class Vendor4(models.Model):
    user = AutoOneToOneField(User, primary_key=True) 
    monthly_order10   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order11   = models.PositiveIntegerField(validators=[MaxValueValidator(45)], default=0, help_text="Max Value is 45")
    monthly_order12   = models.PositiveIntegerField(validators=[MaxValueValidator(25)], default=0, help_text="Max Value is 25")   
    created_at = models.DateTimeField(auto_now=True)
    mod_count = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
    def save(self):
        self.monthly_demand10 = self.user.vendor.monthly_order1
        self.monthly_demand11 = self.user.vendor.monthly_order2
        self.monthly_demand12 = self.user.vendor.monthly_order3
        self.mod_count +=1
        super(Vendor4, self).save()

    

       
    @property
    def monthly_demand4(self):
        return self.monthly_order10+self.monthly_order11+self.monthly_order12    

        
    
    @property
    def actual_demand10(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand4)*.8+.01*(self.monthly_demand4)
        else:
            return (self.monthly_demand4)*.8+.06*(self.monthly_demand4)
    @property
    def actual_demand11(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand4)*.8+.01*(self.monthly_demand4)
        else:
            return (self.monthly_demand4)*.8+.06*(self.monthly_demand4)
    @property
    def actual_demand12(self):
        if self.user.product.style == True | self.user.product.storage==True| self.user.product.durability==True| self.user.product.extended_battery==True: 
            return (self.monthly_demand4)*.8+.01*(self.monthly_demand4)
        else:
            return (self.monthly_demand4)*.8+.06*(self.monthly_demand4)        


   
    
    
    @property
    def inventory10(self):
        return self.monthly_demand4-self.actual_demand10
    @property
    def inventory11(self):
        return self.monthly_demand4-self.actual_demand11
    @property
    def inventory12(self):
        return self.monthly_demand4-self.actual_demand12

    
        

