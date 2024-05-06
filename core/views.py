from django.views.generic import View 
from django.shortcuts import render
##proceso de renderizacion de plantillas HTML

##Aquí se define una nueva clase llamada Home_View 
##que hereda de la clase View. Esto significa que Home_View es una vista genérica de Django.
class Home_View(View):
    def get(self, request, *arg, **kwargs):
        context={
            
        }
        return render(request, "index.html", context)
  
##render toma la solicitud HTTP, una plantilla HTML y un diccionario de contexto opcional como argumentos, y devuelve una respuesta HTTP que representa la plantilla renderizada con el contexto proporcionado.