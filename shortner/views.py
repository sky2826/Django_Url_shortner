from django.shortcuts import render
from .forms import UrlCreateForm
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Url
from django.shortcuts import redirect
# Create your views here.
from django.views.generic import CreateView,DetailView
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect


class UrlCreateView(CreateView):
    form_class=UrlCreateForm
    template_name = "shortner/form.html" 

    def form_invalid(self,form):
    	obj=Url.objects.filter(url=self.request.POST.get('url').lower())
    	if obj.exists():
    		return HttpResponseRedirect("u/"+obj[0].code)
    	else:
    		return super(UrlCreateView,self).form_invalid(form)


class UrlDetailView(DetailView):
	queryset=Url.objects.all()

	def get_object(self,*args,**kwargs):
		code=self.kwargs.get('code')
		obj=get_object_or_404(Url,code=code)
		return obj 


class UrlRedirectDetailView(DetailView):
	
	def get(self,request,*args,**kwargs):
		try:
			url=Url.objects.get(code=self.kwargs.get("code"))
			print(url.url)
			if(url.url[:4]=="http"):
				return redirect(url.url)
			else:
				return HttpResponseRedirect("http://"+url.url)
		except:
			return HttpResponse("error")







