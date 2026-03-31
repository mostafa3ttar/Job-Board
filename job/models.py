from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.

"""
Django Model Field :
    - html widget
    - Validation
    - DB size


"""

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Job(models.Model):  #Class => Table
    title = models.CharField(max_length=100)  # Column
    #location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)    # ONE TO MANY
    exprience = models.IntegerField(default=1)
    img = models.ImageField(upload_to='jobs_img/%y%m%d', null=True, blank=True)
    
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)    ##logic
            self.slug = f"{original_slug}-{str(uuid.uuid4())[:4]}"
        super(Job,self).save(*args, **kwargs)
        
    
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name