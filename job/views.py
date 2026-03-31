from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # context = {'job_list': job_list}  #Template name
    context = {'job_list' : page_obj}  #Template name
    return render(request,'job/job_list.html',context)


def job_detail(request, slug):
    
    job_detail = get_object_or_404(Job, slug=slug)
    
    context = {'job_detail': job_detail}
    
    return render(request, 'job/job_detail.html', context)