from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('cars/', include('apps.cars.urls')),
    path('pricing/', include('apps.pricing.urls')),
    path('users/', include('apps.users.urls')),
    path('washing/', include('apps.washing.urls')),
    
    path('__debug__/', include('debug_toolbar.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)