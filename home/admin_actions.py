# admin_actions.py
import io
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.translation import gettext as _
from django.conf import settings
import os

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = False
    if uri.find("images/") > -1:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
        result = path
    elif uri.find("admin/") > -1:
        path = os.path.join(settings.STATIC_URL, uri.replace(settings.STATIC_URL, ""))
        result = path

    return result




def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result, link_callback=link_callback)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def print_orders(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="orders.pdf"'

    # Create a PDF document
    buffer = io.BytesIO()
    
    for order in queryset:
        pdf = render_to_pdf('order_template.html', {'order': order})
        if pdf:
            response.write(pdf)

    return response

print_orders.short_description = _("Print selected orders")