# admin.py
from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import orders as Orders, units as Units , Customers_num , Thraa_info , Units_num
from django.utils.html import format_html
from django.db.models import Count
from django.http import HttpResponse
from .utils import render_to_pdf
from .resources import OrdersResource
#import export using django-import-export
from import_export.admin import ImportExportModelAdmin

class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('statistics/', self.admin_view(self.statistics_view))
        ]
        return custom_urls + urls

    def statistics_view(self, request):
        # Get units assigned to orders
        assigned_units = Units.objects.filter(orders__isnull=False).values('unit_type').annotate(count=Count('unit_type'))

        # Orders data per day
        orders_data = Orders.objects.extra({'day': "strftime('%%Y-%%m-%%d', date)"}).values('day').annotate(count=Count('units')).order_by('day')

        # Branch data
        branch_data = Orders.objects.values('branch').annotate(count=Count('units__id'))

        # Direct vs Indirect data
        direct_indirect_data = Orders.objects.values('clientSource').annotate(count=Count('units__id'))

        # Dev Sales Manager data
        dev_sales_manager_data = Orders.objects.values('dev_sales_manager').annotate(count=Count('units__id'))

        # Total units from orders
        total_units = Units.objects.filter(orders__isnull=False).count()

        context = dict(
            self.each_context(request),
            units_data=list(assigned_units),
            orders_data=list(orders_data),
            branch_data=list(branch_data),
            direct_indirect_data=list(direct_indirect_data),
            dev_sales_manager_data=list(dev_sales_manager_data),
            total_units=total_units
        )
        return TemplateResponse(request, "admin/statistics.html", context)


admin_site = CustomAdminSite(name='custom_admin')

admin_site = CustomAdminSite(name='custom_admin')

@admin.register(Orders, site=admin_site)
class OrdersAdmin(ImportExportModelAdmin):
    resource_class=OrdersResource
    actions = ["print_orders"]

    def print_orders(self, request, queryset):
        context = {
            'order': queryset,
        }
        pdf = render_to_pdf(request,'order_pdf_template.html', context)
        return pdf

    print_orders.short_description = "Print selected orders"
    
    
    
    
    list_display = (
        'user_details', 
        'clientSource', 'broker_company', 'dev_sales', 'broker_sales', 'dev_sales_manager','branch', 'units_details'
    )
    #filter by client source , date
    list_filter = ('clientSource', 'date')
    
    
    def user_details(self, obj):
        #'customer_num', 'name', 'date', 'phone', 'email',
        html = '<div>'
        html += f'<strong> customer num: {obj.customer_num}</strong><br><strong> date: {obj.date}</strong><br><strong> name: {obj.name}</strong><br><strong>phone: {obj.phone}</strong><br><strong> email: {obj.email}</strong>'
        html += '</div>'
        return format_html(html)
    
    def units_details(self, obj):
        units = obj.units.all()
        html = '<table>'
        for unit in units:
            html += f'<tr><td>{unit.number_of_units}</td><td>{unit.unit_type}</td><td>{unit.floor}</td></tr>'
        html += '</table>'
        return format_html(html)

    units_details.short_description = "Units"

    search_fields = ('name', 'phone', 'email', 'clientSource', 'broker_company')


def delete_unassigned_units(modeladmin, request, queryset):
    # Get the IDs of units that are assigned to orders
    assigned_unit_ids = Orders.objects.values_list('units', flat=True).distinct()
    
    # Filter out units that are not in assigned_unit_ids and delete them
    unassigned_units = Units.objects.exclude(id__in=assigned_unit_ids)
    count, _ = unassigned_units.delete()
    
    modeladmin.message_user(request, f'{count} unassigned units were deleted.')

delete_unassigned_units.short_description = 'Delete units not assigned to any order'


def rewrite_units_number(modeladmin, request, queryset):
    start_number = 1003  # Starting number for EOI1003

    # Order the queryset by the desired field, e.g., 'id' or another field you want to sort by
    ordered_queryset = queryset.order_by('id')

    for index, unit in enumerate(ordered_queryset, start=start_number):
        # Create the new number format
        new_number = f"EOI{index}"
        unit.number_of_units = new_number
        unit.save()

    modeladmin.message_user(request, 'Units numbers rewritten successfully.')


rewrite_units_number.short_description = 'Rewrite units number starting from EOI1003'


@admin.register(Units, site=admin_site)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('number_of_units', 'unit_type', 'floor')
    search_fields = ('unit_type', 'floor')
    actions= [delete_unassigned_units,rewrite_units_number]
    ordering = ['id']

    


@admin.register(Customers_num, site=admin_site)
class Customers_numAdmin(admin.ModelAdmin):
    list_display = ('customer_num',)
    
    
@admin.register(Thraa_info, site=admin_site)
class Thraa_infoAdmin(admin.ModelAdmin):
    list_display = ('broker_company','dev_sale','dev_sale_manager')
    search_fields = ('broker_company','dev_sale','dev_sale_manager')
    list_per_page = 100
    

@admin.register(Units_num, site=admin_site)
class Units_numAdmin(admin.ModelAdmin):
    list_display = ('uints_num',)


from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
#add user , group to new admin
@admin.register(User, site=admin_site)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Group, site=admin_site)
class CustomGroupAdmin(GroupAdmin):
    pass

