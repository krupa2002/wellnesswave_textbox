from dwitter.views import base
from django.urls import path, include

urlpatterns = [
    # Your other URL patterns here
    path('dwitter/', include('dwitter.urls')),
]
