https://django-tailwind.readthedocs.io/en/latest/settings.html

# Projet Django pour LITRevu

Bienvenue dans **Mon Projet Django pour LITRevu** !  
Ce guide vous explique comment configurer et exécuter ce projet Django en local sur votre machine, de l’installation des dépendances à l’accès à l’application.

---

## ✅ Prérequis

Avant de commencer, assurez-vous d’avoir installé :

- [Python](https://www.python.org/downloads/) (version 3.8 ou supérieure)
- [pip](https://pip.pypa.io/en/stable/installation/) (généralement inclus avec Python)
- [Git](https://git-scm.com/downloads)
- [Node.js](https://nodejs.org/) (pour l'utilisation de Tailwind CSS)
- Un éditeur de code (ex : VS Code)

---

## 📥 Configuration de l'environnement local

### 1. Cloner le dépôt

```bash
git clone https://github.com/SebGris/project-9-django-web-LITRevu.git
cd project-9-django-web-LITRevu
```

### 2. Créer un environnement virtuel
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de votre projet.
```bash
python -m venv venv
```

### 3. Activer l'environnement virtuel

Sur Windows :
```bash
venv\Scripts\activate
```
Sur macOS et Linux :
```bash
source venv/bin/activate
```

### 4. Installer les dépendances

Installez les dépendances Python nécessaires en utilisant pip :
```bash
pip install -r requirements.txt
```

### 8. Installer les dépendances Node.js

Assurez-vous d'avoir Node.js installé, puis installez les dépendances nécessaires pour Tailwind CSS.
```bash
npm install
```

### 9. IConstruire les fichiers statiques avec Tailwind CSS

Construisez les fichiers statiques en utilisant Tailwind CSS :
```bash
npm run build
```

### 10. Lancer le serveur de développement

Enfin, lancez le serveur de développement Django :
```bash
python manage.py runserver
```
Ouvrez votre navigateur et accédez à http://127.0.0.1:8000/ pour voir votre application en action.

## 📄 Aide

Accès à l’administration Django : 
👉 http://127.0.0.1:8000/admin/  
Connectez-vous avec le superutilisateur créé précédemment.

Si vous rencontrez des problèmes, vérifiez que :
- l’environnement virtuel est bien activé
- toutes les dépendances sont installées (`pip install -r requirements.txt`)
- vous utilisez la bonne version de Python
- les migrations sont appliquées sans erreur

Sinon, consultez la documentation Django : https://docs.djangoproject.com/fr/

---

## ✨ À propos

Ce projet a été réalisé dans le cadre du parcours **Développeur d'application Python** – OpenClassrooms.
