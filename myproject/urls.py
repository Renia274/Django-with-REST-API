from django.contrib import admin
from django.urls import include, path
from myapp.views import home_view

urlpatterns = [
    # Home page URL mapped to home_view function
    path('', home_view, name='home'),
    
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # API URL patterns included from 'myapp.urls' module
    path('api/', include('myapp.urls')),
]
