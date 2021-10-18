"""Ganaderia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Aplicaciones.Vistas1.views import inicio,categorias, registrarse, seccion,iniciar_seccion
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='index'),
    path('categorias.html',categorias,name='categorias'),
    path('seccion.html',seccion,name='seccion'),
    path('iniciar_seccion.html',iniciar_seccion,name="iniciar_seccion"),
    path('registrarse.html',registrarse,name="registrarse"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)