# 1. Utilisation d’une image Python officielle
FROM python:3.12-slim

# 2. Définition du répertoire de travail
WORKDIR /app

# 3. Installation de Flask
RUN pip install flask

# 4. Copie du fichier app.py dans l’image
COPY app.py .

# 5. Documentation du port utilisé
EXPOSE 5000

# 6. Commande de lancement de l’application
CMD ["python", "app.py"]
