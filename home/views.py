from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import orders , units , Customers_num , Units_num , Thraa_info
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


def home(request):
    # Get customer number
    customer_number_obj = Customers_num.objects.first()
    if not customer_number_obj:
        customer_num = 1002
        sympol = "G"
        Customers_num.objects.create(customer_num=customer_num, sympol=sympol)
    else:
        customer_num = customer_number_obj.customer_num
        sympol = customer_number_obj.sympol

    print("customer number", customer_num)
    customer_num = int(customer_num) + 1
    Customers_num.objects.update(customer_num=customer_num)

    # Get unit number
    unit_number_obj = Units_num.objects.first()
    if not unit_number_obj:
        unit_num = 1003
        unit_sympol = "EOI"
        print('hiiiiiiiii')
        Units_num.objects.create(uints_num=unit_num, sympol=unit_sympol)
    else:
        unit_num = unit_number_obj.uints_num
        unit_sympol = unit_number_obj.sympol
        print('helooooo')

    print('unit number', unit_num)
    unit_num = int(unit_num) + 10
    Units_num.objects.update(uints_num=unit_num)
    thraa=Thraa_info.objects.all()
    # Extract unique dev_sale values 
    unique_dev_sales = set(broker.dev_sale for broker in thraa)    
    
    context = {
        'customer_num': customer_num,
        'sympol': sympol,
        'unit_sympol': unit_sympol,
        'unit_num': unit_num,
        'thraa':thraa,
        'unique_dev_sales': unique_dev_sales
        
    }
    
    

    return render(request, 'index_en.html', context)



def get_dev_sales_manager(request, dev_sale):
    print("dev sale parameter", dev_sale)
    
    # Get dev sales manager based on dev sales from thraa_info table
    dev_sales_manager_obj = Thraa_info.objects.filter(dev_sale=dev_sale).first()

    print("dev_sales_manager_obj", dev_sales_manager_obj)
    
    if dev_sales_manager_obj:
        dev_sales_manager = dev_sales_manager_obj.dev_sale_manager
    else:
        dev_sales_manager = None
        
    print("dev_sales_manager", dev_sales_manager)
    
    # Return JSON response with dev_sales_manager value
    return JsonResponse({'dev_sales_manager': dev_sales_manager})

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
        broker_id = request.POST.get('broker_id', '')

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
            branch=branch,
            broker_id=broker_id
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
    
    
    
    
    
    
    
    
    
 