#!/usr/bin/env bash
# Salir inmediatamente si ocurre un error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Forzar la recopilación limpia de archivos estáticos (Esto creará la carpeta para tu logo)
python manage.py collectstatic --no-input --clear

# 3. Aplicar migraciones de base de datos (por si acaso)
python manage.py migrate