from . import views
from django.urls import path, include

app_name = 'AnalisisData'
urlpatterns = [
    path('',views.dashboard.as_view(), name='dashboard'),
    path('dashboard',views.dashboard.as_view(), name='dashboard'),
    path('tes',views.tes.as_view(), name='tes'),
]