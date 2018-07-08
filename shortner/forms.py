from django import forms 
from .models import Url 
from django.http import HttpResponse,HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class UrlCreateForm(forms.ModelForm):
	class Meta:
		model=Url
		fields=[
		'url' 
		]
	
  
	def clean_url(self):
		validate = URLValidator()
		try:
			validate(self.cleaned_data['url'].lower())
		
		except ValidationError as e:
			raise forms.ValidationError(e)
		obj=Url.objects.filter(url=self.cleaned_data['url'].lower())		
		
		if obj.exists():
			print("m")
			raise forms.ValidationError("Not a valid name")
		else:
			print("q")
			return self.cleaned_data['url'].lower()
    #         obj=Url.objects.get(url=self.cleaned_data.get('url').lower())
    #         return HttpResponseRedirect("u/"+obj.code)
    #     except:
    #         return self.cleaned_data.get('url').lower()