from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')), # Llamado a las URL de la parte web
    path('api/', include('api_app.urls')), # URL de la parte API


    # Esquema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc 
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')

]
