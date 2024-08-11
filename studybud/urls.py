
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse


# username= gopi
# mail = gopi@gmail.com
# password = gopi#143

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))
]
