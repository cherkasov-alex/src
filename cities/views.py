from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import City
from .forms import HtmlForm

def home(request):
   # print(request.POST)
    form = HtmlForm()
    city = request.POST.get('name')
    print(city)
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list':cities, 'form': form})


    class CityDetailView(DetailView):
        queryset = City.objects.all()
        context_object_name = 'object'
        template_name = 'cities/detail.html'


