from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
# Create your models here.

class Rlocation(models.Model): 
    name      =models.CharField(max_length= 120)
    location  =models.CharField(max_length= 120, null=True, blank=True)     
    Timestamp =models.DateTimeField(auto_now=True)
    updated   =models.DateTimeField(auto_now_add=True)
    slug      =models.SlugField(null=True, blank=True)

    def __str__(self):        
	    return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save(sender, instance,*args, **kwargs):
    print("Saving...")
    print(instance.Timestamp)
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

def rl_post_save(sender, instance, *args, **kwargs):
    print("SAVED")    
    print(instance.Timestamp)
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)
        instance.save()

pre_save.connect(rl_pre_save, sender=Rlocation)
post_save.connect(rl_post_save, sender=Rlocation)    
    