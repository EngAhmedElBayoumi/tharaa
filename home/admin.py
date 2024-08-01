# admin.py
from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import orders as Orders, units as Units , Customers_num , Thraa_info , Units_num
from django.utils.html import format_html
from django.db.models import Count


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('statistics/', self.admin_view(self.statistics_view))
        ]
        return custom_urls + urls

    def statistics_view(self, request):
        units_data = Units.objects.values('unit_type').annotate(count=Count('unit_type'))
        orders_data = Orders.objects.extra({'day': "strftime('%%Y-%%m-%%d', date)"}).values('day').annotate(count=Count('id')).order_by('day')

        context = dict(
            self.each_context(request),
            units_data=list(units_data),
            orders_data=list(orders_data),
        )
        return TemplateResponse(request, "admin/statistics.html", context)

admin_site = CustomAdminSite(name='custom_admin')

admin_site = CustomAdminSite(name='custom_admin')

@admin.register(Orders, site=admin_site)
class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'customer_num', 'name', 'date', 'phone', 'email', 
        'clientSource', 'broker_company', 'dev_sales', 'broker_sales', 'dev_sales_manager', 'units_details'
    )
    
    def units_details(self, obj):
        units = obj.units.all()
        html = '<table>'
        for unit in units:
            html += f'<tr><td>{unit.number_of_units}</td><td>{unit.unit_type}</td><td>{unit.floor}</td></tr>'
        html += '</table>'
        return format_html(html)

    units_details.short_description = "Units"

    search_fields = ('name', 'phone', 'email', 'clientSource', 'broker_company')

@admin.register(Units, site=admin_site)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('number_of_units', 'unit_type', 'floor')
    search_fields = ('unit_type', 'floor')

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

