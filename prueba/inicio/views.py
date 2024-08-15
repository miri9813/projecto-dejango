from django.shortcuts import render, HttpResponse


def principal(request):

   return render(request, "inicio/principal.html")

def formulario(resquet):
   
   return render(resquet,"inicio/formulario.html")

def contacto(resquet):
   return render(resquet,"inicio/contacto.html")

def seguridad(resquet,nombre=None):
   nombre = resquet.GET.get('nombre','')
   return render(resquet,"inicio/seguridad.html",
   {'nombre':nombre})

