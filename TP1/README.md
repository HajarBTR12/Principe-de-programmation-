# Service Web SOAP avec JAX-WS

## Description
Ce projet implémente un **service web SOAP** en Java avec JAX-WS.  
Le service expose des opérations simples et permet d'échanger des valeurs primitives et des objets via SOAP.

## Définitions importantes
 **SOAP** : Simple Object Access Protocol
 **JAX-WS** : Java Annotation XML for Web Services
 **JAXB** : Java Architecture XML Building
 **URL** : Uniforme Resource Locator
 **URN** : Uniforme Resource Name
 **URI** : Uniforme Resource Identifier
 **URN + URL = URI**

## Technologies utilisées
 Java 8
 JAX-WS (Java API for XML Web Services)
 JAXB (Java Architecture for XML Binding)
 SOAP (Simple Object Access Protocol)
 SoapUI (pour les tests)

## Structure du projet
```
src/
 ├── Application.java      → Publie le service SOAP
 ├── MonServiceWeb.java    → Définit les opérations du service
 └── Etudiant.java         → Modèle de données étudiant
```

## Déploiement
Le service est publié à l'adresse :  
`http://localhost:888/`

Le fichier WSDL est disponible à :  
`http://localhost:888/?wsdl`

## Opérations disponibles

### convertir(double mt)
Convertit une valeur numérique en la multipliant par 0.9  
 **Entrée :** double  
 **Sortie :** double  

### somme(double a, double b)
Calcule la somme de deux nombres  
 **Entrée :** deux doubles  
 **Sortie :** double  

### getEtudiant(int identifiant)
Retourne un objet étudiant  
**Entrée :** entier (identifiant)  
**Sortie :** objet Etudiant  

