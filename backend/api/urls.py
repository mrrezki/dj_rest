from django.urls import path
from . import views  # form .views import api_home

urlpatterns = [
    path("", views.api_home),  # localhost:8000/api/
    # path('products/', include('products.urls'),
]
