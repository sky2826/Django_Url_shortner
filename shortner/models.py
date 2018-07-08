from django.db import models
from django.core.urlresolvers import reverse
import string
import random
from django.db.models.signals import pre_save, post_save
from .utils import gen_6_digit_random_code



# Create your models here.

class Url(models.Model):
	code = models.CharField(max_length=6,null=True,blank=True)
	url=   models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True)
	# count = models.IntegerField(default=1)

	def __str__(self):
		return self.url 

	def get_absolute_url(self):
		return reverse('detail',kwargs={"code":self.code})





def get_6_digit_code(sender,instance,*args,**kwargs):
	if not instance.code:
		instance.code=gen_6_digit_random_code(instance)



pre_save.connect(get_6_digit_code,sender=Url)