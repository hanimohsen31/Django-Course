from django.urls import path
from . import views

from django.conf.urls import url


urlpatterns = [
    path('', views.joblist),
    path('<int:id>', views.jobdetails),
]
