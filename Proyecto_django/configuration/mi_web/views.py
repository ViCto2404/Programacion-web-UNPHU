from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactoForm
from .models import Articulo, Noticia

def index(request):
    return render(request, 'index.html')

def articulos(request):
    lista_articulos = Articulo.objects.all()
    return render(request, 'articulos.html', {'articulos': lista_articulos})

def bulbasaur(request):
    return render(request, 'bulbasaur.html')

def charmander(request):
    return render(request, 'charmander.html')

def squirtle(request):
    return render(request, 'squirtle.html')

def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias.html', {'noticias': lista_noticias})

def noticia_detalle(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticia_detalle.html', {'noticia': noticia})

def enlaces(request):
    return render(request, 'enlaces.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email_usuario = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            
            # Formatear el correo para incluir la info del remitente real en el cuerpo
            cuerpo_mensaje = f"Has recibido un nuevo mensaje de contacto:\n\n" \
                             f"Nombre: {nombre}\n" \
                             f"Email del remitente: {email_usuario}\n" \
                             f"Asunto: {asunto}\n\n" \
                             f"Mensaje:\n{mensaje}"
            
            try:
                send_mail(
                    f"Contacto Web: {asunto}",
                    cuerpo_mensaje,
                    settings.DEFAULT_FROM_EMAIL, # Remitente fijo (tu cuenta)
                    [settings.DEFAULT_FROM_EMAIL], # Destinatario (tú mismo)
                    fail_silently=False,
                )
                messages.success(request, '¡Gracias! Tu mensaje ha sido enviado correctamente.')
                return redirect('contacto')
            except Exception as e:
                print(f"Error al enviar correo: {e}") # Para depuración si es necesario
                messages.error(request, 'Hubo un error al enviar el mensaje. Inténtalo de nuevo más tarde.')
    else:
        form = ContactoForm()
        
    return render(request, 'contacto.html', {'form': form})

def privacidad(request):
    return render(request, 'privacidad.html')
