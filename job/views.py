from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import ApplyForm, JobForm


# Create your views here.
def joblist(request):
    joblist1 = Job.objects.all()

    paginator = Paginator(joblist1, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'joblist1': page_obj, 'listlength': joblist1 }
    return render(request, 'job/joblist.html', context)


def jobdetails(request, id):
    jobdetail = Job.objects.get(id=id)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jobdetail
            myform.save()
        pass
    else:
        form = ApplyForm()
    context = {'jobdetail': jobdetail, 'form': form}
    return render(request, 'job/jobdetails.html', context)


def addjob(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # myform.job = jobdetail
            # myform.save()
            # main url :: secondary url
            return redirect(reverse('job:job'))
        pass
    else:
        form = JobForm()
    return render(request, 'job/addjob.html', {'form': form})
