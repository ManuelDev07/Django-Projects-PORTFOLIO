from django.shortcuts import render
from Services.models import Services #Para la view de Services

# Create your views here.
def services(request): #Página de servicios que se ofrecen en la web.
    services = Services.objects.all() #Para guardar en una variable todos los servicios de la tabla Services
    
    return render(request, 'services.html', {'services':services})