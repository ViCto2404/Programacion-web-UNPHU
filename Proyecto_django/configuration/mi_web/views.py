from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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

def enlaces(request):
    return render(request, 'enlaces.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            
            # Formatear el correo
            cuerpo_mensaje = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"
            
            try:
                send_mail(
                    asunto,
                    cuerpo_mensaje,
                    email,
                    ['starlin2404@gmail.com'], # Recibes los correos aquí
                    fail_silently=False,
                )
                messages.success(request, '¡Gracias! Tu mensaje ha sido enviado correctamente.')
                return redirect('contacto')
            except Exception as e:
                messages.error(request, 'Hubo un error al enviar el mensaje. Inténtalo de nuevo más tarde.')
    else:
        form = ContactoForm()
        
    return render(request, 'contacto.html', {'form': form})

def privacidad(request):
    return render(request, 'privacidad.html')
