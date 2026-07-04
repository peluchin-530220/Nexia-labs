import os
import requests

from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contacto(request):

    if request.method == "POST":

        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        contenido = f"""
Nuevo mensaje desde NEXIA Labs

Nombre: {nombre}
Correo: {correo}

Mensaje:
{mensaje}
"""

        try:

            api_key = "re_KLzrDNZf_KtEpNW2Ev2WnYMSAm8GMXaVA"

            print("API KEY:", api_key)

            response = requests.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "from": "onboarding@resend.dev",
                    "to": ["nexia.labs1@gmail.com"],
                    "subject": "Nuevo mensaje desde NEXIA Labs",
                    "text": contenido,
                },
                timeout=10,
            )

            print("STATUS:", response.status_code)
            print("RESPUESTA:", response.text)

            if response.status_code in [200, 201, 202]:
                messages.success(
                    request,
                    "Mensaje enviado correctamente."
                )
            else:
                messages.error(
                    request,
                    f"Error Resend: {response.text}"
                )

        except Exception as e:

            print("ERROR:", str(e))
            messages.error(request, f"Error: {str(e)}")

        return redirect("contacto")

    return render(request, "contacto.html")


def sobre(request):
    return render(request, 'sobre.html')