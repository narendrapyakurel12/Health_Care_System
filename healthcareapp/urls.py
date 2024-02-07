from django.urls import path
from .views import *
from .import views

app_name = 'jobapp'
urlpatterns = [
     # HealthCare
    path('', HealthCareHomeView.as_view(), name='jobseekerhome'),
    ]