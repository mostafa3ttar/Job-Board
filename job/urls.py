from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:id>', views.job_detail),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)