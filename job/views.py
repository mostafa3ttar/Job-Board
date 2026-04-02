from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ApplyForm, JobForm

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # context = {'job_list': job_list}  #Template name
    context = {'job_list' : page_obj,
               'total_jobs_count' : job_list.count()}  #Template name 
    return render(request,'job/job_list.html',context)


def job_detail(request, slug):
    
    job_detail = get_object_or_404(Job, slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    
    else:
        form = ApplyForm()
        
    context = {'job_detail': job_detail, 'form': form}
    
    return render(request, 'job/job_detail.html', context)


def add_job(request):
    
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    
    context = {'form': form}
    return render(request, 'job/add_job.html', context)