from django.db import models


class Marketing(models.Model):
				
    offline          = models.PositiveIntegerField(blank=False, default=0)
    online           = models.PositiveIntegerField(blank=False, default=0)
    tv               = models.PositiveIntegerField(blank=False, default=0)
    radio            = models.PositiveIntegerField(blank=False, default=0)
    prints           = models.PositiveIntegerField(blank=False, default=0)
    hr               = models.PositiveIntegerField(blank=False, default=0)
    updated          = models.DateTimeField(auto_now=True)
    timestamp        = models.DateTimeField(auto_now_add=True)
    total_marketing  = models.PositiveIntegerField(blank=False, default=0)
   


class Vendor(models.Model):
    name = models.CharField(max_length=120, unique=True)
    cost_index = models.DecimalField(max_digits=50, blank = False, decimal_places=1)
    delivery_index = models.DecimalField(max_digits=50, blank = False, decimal_places=1)
    quality_index = models.DecimalField(max_digits=50, blank=False, decimal_places=1)
    yearly_binding = models.BooleanField(default=False)
    delivery_time = models.IntegerField(default=30, blank=False, help_text = 'in days')
    rm_cost = models.IntegerField(default=500, blank=False, verbose_name='Per Unit Cost')
    vendor_cost = models.DecimalField(max_digits=50, blank=False, decimal_places=2)

    def __str__(self):
        return self.name 

class Demand(models.Model):
    monthly_demand=models.PositiveIntegerField(default=10000, blank=False)
    demand_inc_value = models.DecimalField(max_digits=50, blank=False, decimal_places=2)
    monthly_inc = models.BooleanField(blank=False, default=False)


class Costs(models.Model):
    infra_cost = models.IntegerField(default=10000, blank=False)
    hr_cost = models.IntegerField(blank=False, default=100)
    marketing_cost = models.IntegerField(blank=True)
    rm_cost_total = models.DecimalField(max_digits=50, blank=False, decimal_places=2)


def total_cost(self):
    total = total_marketing+rm_cost_total+hr_cost+infra_cost
    self.save()
    return self.total 



