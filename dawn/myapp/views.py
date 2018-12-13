from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from random import randint as ri
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView,DetailView
from .models import Rlocation

    
def restaurant_listview(request):
    
 	template_name = 'restaurants/rlocation_list.html'
 	queryset= Rlocation.objects.all()
 	context= {
 	  "object_list": queryset
 	}
 	return render(request, template_name, context)

class RstListview(ListView):
    template_name = 'restaurants/rlocation_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Rlocation.objects.filter(
                
                Q(location__iexact=slug) |
                Q(location__icontains=slug)
                
                )
        else:
            queryset = Rlocation.objects.all()    
        return queryset


class RstDetailView(DetailView):
    template_name = 'restaurants/rlocation_detail.html'
    queryset = Rlocation.objects.all()

    def get_object(self,*args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(Rlocation, id=rest_id)
        return obj
