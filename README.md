# Projet : Service Web SOAP avec JAX-WS

## **Introduction**

Ce projet met en place un **Service Web SOAP** en utilisant **JAX-WS** en Java. Le service permet à des clients d’invoquer différentes méthodes à distance via le protocole **SOAP**, facilitant la communication entre le client et le serveur par des échanges **XML**.

L'objectif de ce projet est de démontrer la mise en œuvre de services Web SOAP en Java, comprendre la communication entre un client et un serveur et utiliser des outils comme **SoapUI** pour tester le service.

## **Technologies utilisées**

- **Java 8** ou version supérieure
- **JAX-WS** : Java API for XML Web Services
- **JAXB** : Java Architecture for XML Binding
- **SOAP** : Simple Object Access Protocol
- **HTTP** : Protocole de communication

## **Structure du projet**

Le projet est composé des fichiers suivants :

- **Application.java** : La classe principale qui publie le service SOAP localement.
- **MonServiceWeb.java** : Contient les opérations du service (comme la conversion de montants et l'addition de nombres).
- **Etudiant.java** : Modèle représentant un étudiant utilisé dans les échanges SOAP.

## **Description du Service Web**

### **MonServiceWeb**
La classe `MonServiceWeb` expose plusieurs méthodes via SOAP :

1. **convertir** : Convertit un montant en le multipliant par 0.9.
2. **somme** : Calcule la somme de deux nombres.
3. **getEtudiant** : Retourne un objet `Etudiant` basé sur un identifiant.

### **Etudiant**
La classe `Etudiant` représente un étudiant avec trois attributs : identifiant, nom, et moyenne. Elle est utilisée pour envoyer des objets `Etudiant` via le service SOAP.

## **Déploiement du Service**

Une fois le projet exécuté, le service est disponible localement à l’adresse :

- **URL du service** : [http://localhost:888/](http://localhost:888/)

Le fichier **WSDL** (Web Service Description Language) est généré automatiquement et peut être consulté à l’adresse suivante :

- **WSDL** : [http://localhost:888/?wsdl](http://localhost:888/?wsdl)

---

## **Instructions pour exécuter le projet**

### **Prérequis** :

- **Java 8** ou version supérieure
- **IntelliJ IDEA** ou un autre IDE Java

### **Étapes d'exécution** :

1. Clonez ou copiez le projet sur votre machine locale.
2. Ouvrez le projet dans **IntelliJ IDEA**.
3. Compilez et exécutez le projet. Le service sera disponible à l'adresse : `http://localhost:888/`.


## **Test du Service Web**

Vous pouvez tester le service avec des outils comme **SoapUI** ou **Postman** en utilisant le fichier **WSDL** pour générer des requêtes SOAP. Vous pourrez tester les méthodes exposées comme :

- **`convertir`** : Convertir un montant en appliquant un facteur de 0.9.
- **`somme`** : Additionner deux nombres.
- **`getEtudiant`** : Obtenir un étudiant en fonction de son identifiant.


## **Conclusion**

Ce projet illustre la mise en place d'un **Service Web SOAP** simple avec **JAX-WS** et **JAXB** en Java. Il permet de comprendre le fonctionnement des échanges SOAP, l’utilisation du WSDL pour la communication et la gestion des objets complexes via XML.


