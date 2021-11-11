from django.shortcuts import render
from .models import Job


# Create your views here.
def joblist(request):
    joblist1 = Job.objects.all()
    context = {'joblist1': joblist1}
    return render(request, 'job/joblist.html', context)


def jobdetails(request, id):
    jobdetail = Job.objects.get(id=id)
    context = {'jobdetail': jobdetail}
    return render(request, 'job/jobdetails.html', context)
