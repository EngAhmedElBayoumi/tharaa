from import_export import resources
from .models import orders

class OrdersResource(resources.ModelResource):
    class Meta:
        model = orders