from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medica_app.urls')), # Llamado a las URL de la parte web
    path('api/', include('api_app.urls')) # URL de la parte API
]
