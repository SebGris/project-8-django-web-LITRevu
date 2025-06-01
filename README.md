
# Mon Projet Django pour LITRevu

## 🚀 Introduction

Bienvenue dans **Mon Projet Django pour LITRevu** !  
Ce guide vous expliquera comment configurer et exécuter ce projet Django en local sur votre machine.

---

## ✅ Prérequis

Avant de commencer, assurez-vous d'avoir les outils suivants installés :

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/)
- Un éditeur de code (ex : VS Code)
- Un environnement virtuel Python (recommandé)

---

## 📥 Installation et configuration locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/SebGris/project-9-django-web-LITRevu.git
cd project-9-django-web-LITRevu
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv env
env\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ⚙️ Quelques commandes et procédures Django

### 📥 Installez Django avec pip

#### 1. Ouvrir un terminal.

Créer un répertoire pour l'application web Django.

```bash
mkdir project-9-django-web-LITRevu
cd project-9-django-web-LITRevu
```
Optionnel : si vous suivez ce projet dans Git, c'est là que nous initialiserons notre repository.

```bash
git init
```

#### 2. Créer un environnement virtuel.

```bash
python -m venv env
```

#### 3. Activer l'environnement virtuel.

```bash
.venv\Scripts\activate.bat
```

#### 4. Installez Django avec pip

```bash
pip install django
```

### 🛠️ Initialisation de la base de données

Appliquez les migrations pour créer les tables nécessaires :

```bash
python manage.py migrate
```

---

### 👤 Création d’un superutilisateur

Pour accéder à l’interface d’administration Django :

```bash
python manage.py createsuperuser
```

Suivez les instructions pour définir un nom d’utilisateur, une adresse email et un mot de passe.

---

### ▶️ Lancer le serveur de développement

```bash
python manage.py runserver
```

L’application sera alors disponible à l’adresse suivante :  
👉 http://127.0.0.1:8000/

---

### 🔑 Accès à l’administration Django

👉 http://127.0.0.1:8000/admin/  
Connectez-vous avec le superutilisateur que vous avez créé précédemment.

---

### 🧪 Tests (optionnel)

Pour exécuter les tests unitaires :

```bash
python manage.py test
```

---

## 📄 Aide

Si vous rencontrez des problèmes, assurez-vous que :
- l’environnement virtuel est bien activé
- toutes les dépendances sont installées
- vous utilisez la bonne version de Python

Sinon, consultez la documentation Django : https://docs.djangoproject.com/fr/

---

## ✨ À propos

Ce projet a été réalisé dans le cadre du parcours **Développeur d'application Python** – OpenClassrooms.
