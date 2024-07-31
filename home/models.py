from django.db import models
import datetime
# Create your models here.

class units(models.Model):
    number_of_units=models.CharField(max_length=50,default="EOI1003")
    unit_type=models.CharField(max_length=100)
    floor=models.CharField(max_length=100)
    
    def __str__(self):
        return f'numer: {self.number_of_units}, type: {self.unit_type}, floor: {self.floor}'



class orders(models.Model):
    date=models.DateField(default=datetime.datetime.now)
    customer_num=models.CharField(max_length=50,default="G1002")
    name=models.CharField(max_length=50)
    birthday=models.CharField(max_length=100)
    national_id=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    occupation=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    email=models.EmailField()
    clientSource=models.CharField(max_length=50)
    broker_company=models.CharField(max_length=50)
    dev_sales=models.CharField(max_length=50)
    broker_sales=models.CharField(max_length=50)
    broker_id=models.CharField(max_length=50)
    dev_sales_manager=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    units=models.ManyToManyField(units)
    
    
    def __str__(self):
        return f'customer_num: {self.customer_num}, name: {self.name}'
    
    class Meta:
        # order by customer number
        ordering = ['customer_num']
        
        
class Customers_num(models.Model):
    customer_num=models.CharField(max_length=50,default="1002")
    sympol=models.CharField(max_length=10,default="G")
    
    
    
class Units_num(models.Model):
    uints_num=models.CharField(max_length=50,default="1003")
    sympol=models.CharField(max_length=10,default="EOI")


    
class Thraa_info(models.Model):
    broker_company=models.CharField(max_length=10000)
    dev_sale=models.CharField(max_length=10000)
    dev_sale_manager=models.CharField(max_length=10000)
    
    def __str__(self):
        return f'company :{self.broker_company}'
    

    


