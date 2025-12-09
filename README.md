# 🏠 Home I/O Data Collection & Analysis Project

Ce projet met en œuvre une chaîne complète de traitement de données IoT : de la collecte de données en temps réel via une simulation domotique (Home I/O) jusqu'à l'analyse prédictive et la modélisation.

Le but principal est de prédire la **température intérieure** d'une maison intelligente en fonction de paramètres environnementaux (température extérieure, ouverture des portes, humidité, etc.).

## 📂 Contenu du dépôt

* **`src/`** : Contient les scripts Python pour l'interrogation du serveur Home I/O et la récupération des données.
* **`data/`** : Jeux de données collectés (CSV) utilisés pour l'entraînement et le test.
* **`docs/`** : Documentation technique du serveur et **Rapport complet du projet**.

## 🚀 Fonctionnalités

1.  **Collecte de données (Data Mining)** :
    * Script Python (`CSVrecup.py`) qui interroge l'API REST locale de Home I/O (`http://localhost:9797/poll`).
    * Récupération des métriques : Température (Int/Ext), état des portes, humidité, heure, vitesse du vent.
    * Conversion et nettoyage des données (ex: Kelvin vers Celsius).
    * Stockage au format CSV.

2.  **Analyse et Modélisation (Machine Learning)** :
    * Approche par **Régression Linéaire**.
    * Comparaison de modèles : Modèle simple (Temp Ext seulement) vs Modèle multivarié.
    * Calcul des performances (MSE, R² Score).

## 🛠️ Prérequis

* Python 3.x
* Logiciel [Home I/O](https://realgames.co/home-io/) (pour la collecte de nouvelles données)

## 📦 Installation

1.  Clonez ce dépôt :
    ```bash
    git clone [https://github.com/RostomS/homeio-iot-project.git](https://github.com/RostomS/homeio-iot-project.git)
    cd homeio-iot-project
    ```

2.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Utilisation

### Pour collecter des données :
1.  Lancez le logiciel **Home I/O** et assurez-vous que le serveur Web est actif (Port 9797 par défaut).
2.  Exécutez le script de récupération :
    ```bash
    python src/CSVrecup.py
    ```
3.  Le script affichera `📡 Début de la collecte...` et enregistrera les données dans un fichier CSV.

## 📊 Résultats (Extrait du rapport)

Le modèle de régression linéaire multivarié a permis d'obtenir les résultats suivants sur le jeu de données de test :

* **MSE (Mean Squared Error)** : ~23.98
* **Score R²** : ~0.61
* **Variables influentes** : Température extérieure, État des portes (F1/F2), Humidité.

Pour plus de détails sur les équations et les graphiques de prédiction, consultez le fichier `docs/Rapport projet IOT.pdf`.

## 👥 Auteurs

* **El Yazid Benzidane**
* **Rostom Samar**

---
*Projet réalisé dans le cadre d'un module universitaire IoT.*
