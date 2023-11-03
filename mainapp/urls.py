from django.urls import path
from .import views
app_name='mainapp'

urlpatterns = [
    path('',views.Home, name='home'),
    path('features',views.features, name='features'),
]