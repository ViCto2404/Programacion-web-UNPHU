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
            
            cuerpo_mensaje = f"Has recibido un nuevo mensaje de contacto:\n\n" \
                             f"Nombre: {nombre}\n" \
                             f"Email del remitente: {email_usuario}\n" \
                             f"Asunto: {asunto}\n\n" \
                             f"Mensaje:\n{mensaje}"
            
            try:
                # Usamos EMAIL_HOST_USER para autenticar el envío (From)
                # Usamos DEFAULT_FROM_EMAIL para recibir el correo (To)
                send_mail(
                    f"Contacto Web: {asunto}",
                    cuerpo_mensaje,
                    settings.EMAIL_HOST_USER,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, '¡Gracias! Tu mensaje ha sido enviado correctamente.')
                return redirect('contacto')
            except Exception as e:
                # Esto imprimirá el error real en tu consola de VS Code/Terminal
                print(f"--- ERROR DE SMTP ---: {e}")
                messages.error(request, f'Error al enviar el mensaje. Asegúrate de que tu "Contraseña de Aplicación" de Google sea correcta.')
        else:
            messages.error(request, 'Por favor, revisa los datos del formulario.')
    else:
        form = ContactoForm()
        
    return render(request, 'contacto.html', {'form': form})

def privacidad(request):
    return render(request, 'privacidad.html')
