<<<<<<< HEAD
# APIs REST Flask — Étudiants & Livres

Deux petites APIs REST en Python avec Flask, les données sont stockées en mémoire (pas de base de données).

## Fichiers

- `API_REST_py.py` : API de gestion des étudiants
- `rest_livres.py` : API de gestion des livres

## Installation

```bash
pip install flask
```

## Lancer les serveurs

```bash
python API_REST_py.py
# ou
python rest_livres.py
```


## API Étudiants

- `GET /students` : récupérer tous les étudiants
- `GET /students/<id>` : récupérer un étudiant par son ID
- `POST /students` : ajouter un étudiant
- `PUT /students/<id>` : modifier un étudiant
- `DELETE /students/<id>` : supprimer un étudiant

## API Livres

- `GET /livres` : récupérer tous les livres
- `GET /livres/<id>` : récupérer un livre par son ID
- `POST /livres` : ajouter un livre
- `PUT /livres/<id>` : modifier un livre
- `DELETE /livres/<id>` : supprimer un livre
- `GET /livres/count` : nombre total de livres
- `GET /livres/count/<annee>` : nombre de livres publiés une année donnée

## Remarque

Les données sont remises à zéro à chaque redémarrage du serveur.
=======
# PHP Students

Application PHP qui consomme une API REST Flask pour gérer des étudiants.

## Prérequis

- PHP 8.0+
- API Flask qui tourne sur `http://127.0.0.1:5000`

## Lancer le projet

```bash
# 1. Démarrer l'API Flask
python app.py

# 2. Démarrer le serveur PHP
cd php/
php -S localhost:8000
```

Ouvrir ensuite : `http://localhost:8000/index.php?action=list`

## Structure

```
php/
├── index.php
├── config/
│   └── config.php
├── services/
│   └── StudentService.php
├── views/
│   ├── students.php
│   ├── student_show.php
│   └── student_form.php
├── assets/
│   └── style.css
└── tests/
    ├── test_api_1.php
    ├── test_api_2.php
    ├── test_api_3.php
    ├── test_api_4.php
    └── test_api_5.php
```

## Routes

| URL | Action |
|-----|--------|
| `?action=list` | Liste tous les étudiants |
| `?action=show&id=X` | Détail d'un étudiant |
| `?action=create` | Ajouter un étudiant |
| `?action=edit&id=X` | Modifier un étudiant |
| `?action=delete&id=X` | Supprimer un étudiant |

## Configuration

Modifier l'URL de l'API dans `config/config.php` si besoin :

```php
define('API_BASE_URL', 'http://127.0.0.1:5000');
```
>>>>>>> 3a9541de719071dce23cf0f26a5336492da84607
