from django.shortcuts import render
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from .models import Alumnos
import datetime
from django.shortcuts import get_object_or_404
#Accedemos al modelo Alumnos que contiene la estructura de la tabla.
# Create your views here.
def registro(request):

    alumnos=Alumnos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registro/principal.html",{'alumnos':alumnos})
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#si los datos recibidos son correctos
            form.save()#inserta
            return render(request,'registro/contacto.html')
    form = ComentarioContactoForm()

    return render(request,'registro/contacto.html',{'form':form})

def contacto(resquet):
   return render(resquet,"registro/contacto.html")

def consultarComentarios(request):
    ComentariosContactos = ComentarioContacto.objects.all()
    return render(request, "registro/consultarComentario.html", {'ComentariosContactos': ComentariosContactos})

def elimanrComentarioContacto(request, id,
    confirmacion='registro/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registro/ConsultarComentario.html", {'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})
    

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
#get permite establecer una condicionante a la consulta y recupera el objetos
#del modelo que cumple la condición (registro de la tabla ComentariosContacto.
#get se emplea cuando se sabe que solo hay un objeto que coincide con su
#consulta.
    return render(request,"registro/formEditComentario.html", {'comentario':comentario})

#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados.

def consultasSQL(request):

    alumnos=Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen FROM registro_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request,"registro/consultas.html", {'alumno':alumnos})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
#Referenciamos que el elemento del formulario pertenece al comentario
# ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registro/ConsultarComentario.html", {'comentarios':comentarios})

#Si el formulario no es valido nos regresa al formulario para verificar
#datos
    return render(request,"registro/formEditComentario.html",  {'comentario':comentario})



def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__int=["Juan" , "Ana"])
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2024, 7 , 17)
    fechaFin = datetime.date(2024, 7 , 17)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request, "registro/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(ComentarioContacto__coment__contains="No inscrito")
    return render(request, "registro/consultas.html",{'alumnos':alumnos})