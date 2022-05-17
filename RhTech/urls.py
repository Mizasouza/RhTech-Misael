
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('rh/', include('rh.urls')),
    path('admin/', admin.site.urls),

]
