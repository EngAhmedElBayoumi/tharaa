from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import orders , units , Customers_num
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    # get Customers_num 
    customer_num = Customers_num.objects.first().customer_num
    customer_num += 1
    Customers_num.objects.update(customer_num=customer_num)
    
    return render(request, 'index_en.html', {'customer_num': customer_num})





@csrf_exempt
def order(request):
    if request.method == 'POST':
        # Extract order data
        date = request.POST.get('date', datetime.datetime.now())
        customer_num = request.POST.get('customer_num')
        name = request.POST.get('name', '')
        birthday = request.POST.get('birthday', '')
        national_id = request.POST.get('national_id', '')
        phone = request.POST.get('phone', '')
        mobile = request.POST.get('mobile', '')
        occupation = request.POST.get('occupation', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        clientSource = request.POST.get('clientSource', '')
        broker_company = request.POST.get('broker_company', '')
        dev_sales = request.POST.get('dev_sales', '')
        broker_sales = request.POST.get('broker_sales', '')
        dev_sales_manager = request.POST.get('dev_sales_manager', '')
        branch = request.POST.get('branch', '')

        # Create the order
        new_order = orders.objects.create(
            date=date,
            customer_num=customer_num,
            name=name,
            birthday=birthday,
            national_id=national_id,
            phone=phone,
            mobile=mobile,
            occupation=occupation,
            address=address,
            email=email,
            clientSource=clientSource,
            broker_company=broker_company,
            dev_sales=dev_sales,
            broker_sales=broker_sales,
            dev_sales_manager=dev_sales_manager,
            branch=branch
        )

        # Parse units JSON string into Python list
        units_json = request.POST.get('units', '[]')
        units_data = json.loads(units_json)

        # Create units and associate them with the order
        for unit_data in units_data:
            new_unit = units.objects.create(
                number_of_units=unit_data.get('number_of_units'),
                unit_type=unit_data.get('type'),
                floor=unit_data.get('Floor')
            )
            new_order.units.add(new_unit)

        return HttpResponse("Order and units created successfully.")
    else:
        return HttpResponse("This endpoint only accepts POST requests.", status=405)