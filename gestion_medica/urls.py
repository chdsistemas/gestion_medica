from django.contrib import admin
from django.urls import path, include
from medica_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medica_app.urls')),
    path('api/', include('api_app.urls'))
]
