from django.shortcuts import render
import datetime
from django.http import HttpResponse
from .models import orders , units , Customers_num , Units_num , Thraa_info
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
#import redirect , reverse
from django.shortcuts import redirect
from django.urls import reverse
from django.db import transaction

@transaction.atomic
def home(request):
    # Get customer number
    customer_number_obj = Customers_num.objects.select_for_update().first()
    if not customer_number_obj:
        customer_num = 1002
        sympol = "G"
        Customers_num.objects.create(customer_num=customer_num, sympol=sympol)
    else:
        customer_num = customer_number_obj.customer_num
        sympol = customer_number_obj.sympol

    customer_num = int(customer_num) + 1
    print("customer number", customer_num)
    
    Customers_num.objects.update(customer_num=customer_num)
    print("customer number", customer_num)
    # Get unit number
    unit_number_obj = Units_num.objects.select_for_update().first()
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
    unit_num = int(unit_num) + 1
    Units_num.objects.update(uints_num=unit_num)
    thraa = Thraa_info.objects.all()
    # Extract unique dev_sale values 
    unique_dev_sale_manager = set(broker.dev_sale_manager for broker in thraa)    
    print("unique_dev_sale_manager", unique_dev_sale_manager)
    context = {
        'customer_num': customer_num,
        'sympol': sympol,
        'unit_sympol': unit_sympol,
        'unit_num': unit_num,
        'thraa': thraa,
        'unique_dev_sale_manager': unique_dev_sale_manager
    }
    
    return render(request, 'index_EN.html', context)

def get_all_dev_sales_manager(request):
    # Get all dev sales manager
    dev_sales_manager_obj = Thraa_info.objects.values_list('dev_sale_manager', flat=True).distinct()
    print("dev_sales_manager", dev_sales_manager_obj)
    
    # create array with dev sales manager without duplicates
    dev_sales_manager = []
    for obj in dev_sales_manager_obj:
        if obj not in dev_sales_manager:
            dev_sales_manager.append(obj)
     
    print("dev_sales_manager", dev_sales_manager)
    return JsonResponse({'dev_sales_manager': dev_sales_manager})



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


from django.db.models import Q
from django.db.models import Func, F


class Trim(Func):
    function = 'TRIM'
    template = "%(function)s(%(expressions)s)"

def get_broker_company_details(request, company_name):
    company_name = company_name.strip()

    # Annotate the queryset with trimmed broker_company and filter
    broker_company_obj = Thraa_info.objects.annotate(
        trimmed_broker_company=Trim(F('broker_company'))
    ).filter(trimmed_broker_company__iexact=company_name).first()
    print("broker_company_obj", broker_company_obj)
    
    # Get all dev_sale_manager that belong to the broker company
    dev_sales_manager_obj = Thraa_info.objects.annotate(
        trimmed_broker_company=Trim(F('broker_company'))
    ).filter(trimmed_broker_company__iexact=company_name)
    print("dev_sales_manager_obj", dev_sales_manager_obj)
    
    dev_sale_managers = [obj.dev_sale_manager for obj in dev_sales_manager_obj]
    
    broker_company_id = broker_company_obj.broker_company_id if broker_company_obj else None
    
    context = {
        'broker_company_id': broker_company_id,
        'dev_sale_managers': dev_sale_managers
    }
    
    return JsonResponse(context)


def get_dev_sales_manager_details(request, dev_sales_manager):
    print("dev sales manager parameter", dev_sales_manager)
    
    # Get dev sales based on dev sales manger from thraa_info table
    dev_sales_manager_obj = Thraa_info.objects.filter(dev_sale_manager=dev_sales_manager)
    
    

    print("dev_sales_manager_obj", dev_sales_manager_obj)
    
    # create array of dev sales without duplicates
    dev_sales = []
    for obj in dev_sales_manager_obj:
        if obj.dev_sale not in dev_sales:
            dev_sales.append(obj.dev_sale)
        
    print("dev_sales", dev_sales)
    
    # Return JSON response with dev_sales value
    return JsonResponse({'dev_sales': dev_sales})
    






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
        broker_company = request.POST.get('broker_company', 'no results')
        broker_company_id = request.POST.get('broker_company_id', 'no results')
        dev_sales = request.POST.get('dev_sales', '')
        broker_sales = request.POST.get('broker_sales', '')
        dev_sales_manager = request.POST.get('dev_sales_manager', '')
        branch = request.POST.get('branch', '')
        broker_id = request.POST.get('broker_id', '')
        ambassador_name = request.POST.get('ambassador_name', 'no results')
        ambassador_id = request.POST.get('ambassador_id', 'no results')
        ambassador_phone = request.POST.get('ambassador_phone', 'no results')
        ambassador_email = request.POST.get('ambassador_email', 'no results')
        amount = request.POST.get('amount', '')
        payment= request.POST.get('payment', '')

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
            broker_company_id=broker_company_id,
            dev_sales=dev_sales,
            broker_sales=broker_sales,
            dev_sales_manager=dev_sales_manager,
            branch=branch,
            broker_id=broker_id,
            ambassador_name=ambassador_name,
            ambassador_id=ambassador_id,
            ambassador_phone=ambassador_phone,
            ambassador_email=ambassador_email,
            amount=amount,
            payment_method=payment
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
    
    
    
    
    
import csv
import io
    
    
    
 # add data from csv file in tharaa_info table first row is header so we need to skip it first column is broker_company_id and second column is broker_company , third column is dev_sale and fourth column is dev_sale_manager
def upload_data_from_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            return JsonResponse({'error': 'Invalid file format. Only CSV files are allowed.'})

        # Read the CSV file
        data_set = csv_file.read().decode('utf-8-sig')  # Use 'utf-8-sig' to handle BOM (Byte Order Mark) for UTF-8 files
        io_string = io.StringIO(data_set)
        csv_reader = csv.reader(io_string, delimiter=',', quotechar='"')

        # Skip the header row
        next(csv_reader)

        for row in csv_reader:
            # Ensure there are exactly 4 columns
            if len(row) < 4:
                continue  # Skip rows with insufficient columns

            broker_company_id = row[0].strip() if row[0].strip() else None
            broker_company = row[1].strip() if row[1].strip() else None
            dev_sale = row[2].strip() if row[2].strip() else None
            dev_sale_manager = row[3].strip() if row[3].strip() else None

            # Use update_or_create to handle both creation and updating of records
            _, created = Thraa_info.objects.update_or_create(
                broker_company_id=broker_company_id,
                broker_company=broker_company,
                defaults={
                    'dev_sale': dev_sale,
                    'dev_sale_manager': dev_sale_manager
                }
            )

        return JsonResponse({'message': 'Data uploaded successfully.'})

    return render(request, 'upload_data_from_csv.html')
 

 
def handler404(request, exception):
    
    url = reverse('home:home')
    #redirect to home page
    return redirect(url)
    