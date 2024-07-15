from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include("clientes.urls")),
    path('autos/', include('autos.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)