import os
import requests

from django.shortcuts import render, redirect
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

            response = requests.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {os.environ.get('RESEND_API_KEY')}",
                    "Content-Type": "application/json"
                },
                json={
                    "from": "onboarding@resend.dev",
                    "to": "nexia.labs1@gmail.com",
                    "subject": "Nuevo mensaje desde la web",
                    "text": contenido,
                },
                timeout=5
            )

            if response.status_code == 200:
                messages.success(request, 'Mensaje enviado correctamente')
            else:
                messages.error(request, f'Error: {response.text}')

        except Exception as e:

            messages.error(request, f'Error: {e}')

        return redirect('contacto')

    return render(request, 'contacto.html')


def sobre(request):
    return render(request, 'sobre.html')