from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postss.urls', namespace='postss'))
]


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_to=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_to=settings.MEDIA_ROOT)
    
