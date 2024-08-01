from django.contrib import admin 
from django.urls import path, include 
 
#import settings
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# import set_language
from django.views.i18n import set_language
#handel404 , handel500
from django.conf.urls import handler404, handler500 
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from home.admin import admin_site

urlpatterns = [ 
    path('admin/', admin_site.urls), 
    
    path('', include('home.urls')), 
    path('i18n/', set_language, name='set_language'),

] 

urlpatterns += i18n_patterns(
    path('', include('home.urls')),
    path('i18n/', set_language, name='set_language'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



admin.site.index_title=_('Tharaa Dashboard')
admin.site.site_header=_('Tharaa Dashboard')
admin.site.site_title=_('Tharaa Dashboard')

handler404 = 'home.views.handler404'
