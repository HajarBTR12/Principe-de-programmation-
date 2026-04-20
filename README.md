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
