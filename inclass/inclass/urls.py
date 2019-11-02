
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('login/', include('frontend.urls')),
    path('toModel/', include('frontend.urls')),
    path('modeling/', include('frontend.urls')),
    path('api/', include('turmas.urls'))
    

]
