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
    broker_company=models.CharField(max_length=50,null=True,blank=True)
    broker_company_id=models.CharField(max_length=50,null=True,blank=True)
    dev_sales=models.CharField(max_length=50,null=True,blank=True)
    broker_sales=models.CharField(max_length=50,null=True,blank=True)
    broker_id=models.CharField(max_length=50)
    dev_sales_manager=models.CharField(max_length=50,null=True,blank=True)
    branch=models.CharField(max_length=50)
    ambassador_name=models.CharField(max_length=100,null=True,blank=True)
    ambassador_id=models.CharField(max_length=100,null=True,blank=True)
    ambassador_phone=models.CharField(max_length=100,null=True,blank=True)
    ambassador_email=models.CharField(max_length=100,null=True,blank=True)
    amount=models.CharField(max_length=100,null=True,blank=True)
    units=models.ManyToManyField(units)
    payment_method=models.CharField(max_length=100,null=True,blank=True,default="cash")
    
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
    
    def __str__(self):
        return f'{self.sympol}{self.uints_num}'
    
    class Meta:
        verbose_name = 'EOI Number'
        verbose_name_plural = 'EOI Number'


    
class Thraa_info(models.Model):
    broker_company=models.CharField(max_length=10000,null=True,blank=True)
    broker_company_id=models.CharField(max_length=10000,null=True,blank=True)
    dev_sale=models.CharField(max_length=10000,null=True,blank=True)
    dev_sale_manager=models.CharField(max_length=10000,null=True,blank=True)
    
    def __str__(self):
        return f'company :{self.broker_company}'
    
    class Meta:
        # order by customer number
        ordering = ['id']
        verbose_name = 'Borkers_info'
        verbose_name_plural = 'Borkers_info'
    


