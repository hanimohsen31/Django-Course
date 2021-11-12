from django.urls import path
from . import views
app_name = 'job'
from django.conf.urls import url


urlpatterns = [
    path('', views.joblist, name='joblist'),
    path('index.html', views.joblist, name='joblist'),
    path('add', views.addjob, name='add'),
    path('<int:id>', views.jobdetails, name='job_details'),
]


