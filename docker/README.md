# Conteneurisation d’une API REST avec Docker

## Introduction

Dans ce projet, l’objectif est de conteneuriser une API Flask avec Docker afin d’exécuter l’application dans un environnement isolé contenant toutes les dépendances nécessaires.

---

## Création du Dockerfile

Créer un fichier nommé `Dockerfile` à la racine du projet.

```dockerfile
FROM python:3.12-slim

WORKDIR /ProjetAPI

RUN pip install flask mysql-connector-python

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## Explication du Dockerfile

### FROM python:3.12-slim

Cette instruction permet d’utiliser une image Python légère avec Python 3.12 déjà installé.

### WORKDIR /ProjetAPI

Définit le dossier principal de travail dans le conteneur.

### RUN pip install flask mysql-connector-python

Installe les dépendances nécessaires au projet :

- Flask : framework utilisé pour créer l’API REST
- mysql-connector-python : permet la connexion avec MySQL

### COPY . .

Copie tous les fichiers du projet dans le conteneur Docker.

### EXPOSE 5000

Indique que l’application fonctionne sur le port 5000.

### CMD ["python", "app.py"]

Lance automatiquement l’application Flask au démarrage du conteneur.

---

## Construction de l’image Docker

Pour construire l’image Docker :

```bash
docker build -t mon_api .
```

---

## Exécution du conteneur

Commande pour démarrer le conteneur :

```bash
docker run -p 4900:5000 mon_api
```

Le port `4900` de la machine locale est relié au port `5000` du conteneur.

---

## Publication sur Docker Hub

### Connexion à Docker Hub

```bash
docker login
```

### Ajouter un tag à l’image

```bash
docker tag mon_api sabrina0324/mon_api:1
```

### Envoyer l’image sur Docker Hub

```bash
docker push sabrina0324/mon_api:1
```

---

## Utilisation de Docker Compose

Docker Compose permet de lancer plusieurs services automatiquement :

- l’API Flask
- la base de données MySQL

### Fichier docker-compose.yml

```yaml
services:
  db:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ""
      MYSQL_DATABASE: school_api
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  api:
    build:
      context: .
    restart: unless-stopped
    depends_on:
      - db
    ports:
      - "5000:5000"

volumes:
  mysql_data:
```

---

## Démarrage des conteneurs

```bash
docker compose up --build
```

---

## Vérification de l’API

Après le lancement des conteneurs, l’API est accessible à l’adresse suivante :

```bash
http://localhost:5000/students
```

---

## Conclusion

La conteneurisation avec Docker facilite le déploiement et l’exécution de l’API Flask.  
Docker Compose permet également de gérer facilement plusieurs services comme l’API et la base de données MySQL.
