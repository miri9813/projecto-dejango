"""
URL configuration for CursoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registro import views as views_registro

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('formulario/', views.formulario, name="Formulario"),
    path('contacto/', views.contacto, name="Contactanos"),
    path('seguridad/', views.seguridad, name="Seguridad"),
    path('',views_registro.registro, name="Principal"),    
    path('contactoo/', views_registro.contacto, name="Contactanos"),
    path('registro/', views_registro.registrar, name="Registrar"),
    path('consultarComentario/', views_registro.consultarComentarios, name="Consultar"),
    path('eliminarComentario/<int:id>', views_registro.elimanrComentarioContacto, name="Eliminar"),
    path('formEditComentario/<int:id>/', views_registro.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registro.editarComentarioContacto, name='Editar'),
    path('consultasSQL',views_registro.consultasSQL,name="sql"),
    path('consultas1/', views_registro.consultar1, name="Consultas1"),
    path('consultas2/', views_registro.consultar2, name="Consultas2"),
    path('consultas3/', views_registro.consultar3, name="Consultas3"),
    path('consultas4/', views_registro.consultar4, name="Consultas4"),
    path('consultas5/', views_registro.consultar5, name="Consultas5"),
    path('consultas6/', views_registro.consultar6, name="Consultas6"),
    path('consultas7/', views_registro.consultar7, name="Consultas7"),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
             document_root=settings.MEDIA_ROOT)             