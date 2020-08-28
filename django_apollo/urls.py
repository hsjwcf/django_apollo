
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apollo_app/',include("apollo_app.urls")), #包含应用的urls文件

]
