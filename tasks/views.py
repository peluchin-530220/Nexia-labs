import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contacto(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        contenido = f"""
Nuevo mensaje desde NEXIA Labs

Nombre: {nombre}
Correo: {correo}

Mensaje:
{mensaje}
"""

        try:

            send_mail(
                subject='Nuevo mensaje desde la web',
                message=contenido,
                from_email=os.environ.get('EMAIL_HOST_USER'),
                recipient_list=['nexia.labs1@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Mensaje enviado correctamente')

        except Exception as e:

            messages.error(request, f'Error al enviar: {e}')

        return redirect('contacto')

    return render(request, 'contacto.html')


def sobre(request):
    return render(request, 'sobre.html')