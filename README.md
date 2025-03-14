# Blog Django

## Description
Ce projet est une application web de blog construite avec Django. Il permet aux utilisateurs de publier, modifier et commenter des articles.

## Fonctionnalités
- Authentification des utilisateurs (inscription, connexion, mot de passe oublié)
- Création, modification et suppression d'articles de blog
- Système de commentaires sous chaque article
- Catégorisation des articles par tags et catégories
- Interface utilisateur réactive et intuitive
- Gestion des médias (images, fichiers joints aux articles)

### Fonctionnalités à venir
- Système de likes
- Ajout aux favoris
- Consultation des profils des utilisateurs
- Page de profil utilisateur

## Technologies utilisées
- **Backend** : Django, Django REST Framework
- **Base de données** : PostgreSQL / SQLite (selon l'environnement)
- **Frontend** : HTML, CSS, Bootstrap
- **Autres** : Sendinblue API (pour les emails), Cloudinary (pour la gestion des médias)

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ZieTech-dev/my-django-blog.git
   cd my-django-blog
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate  # Sur Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```
   Accédez à l'application via [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Configuration des variables d'environnement
Créez un fichier `.env` à la racine du projet et ajoutez-y :
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # Ou PostgreSQL
   SENDINBLUE_API_KEY=your_sendinblue_api_key
   ```

## Déploiement
Pour le déploiement sur un serveur (ex: Heroku, Render, DigitalOcean) :
- Configurez les fichiers `settings.py` pour utiliser les variables d'environnement
- Utilisez `gunicorn` comme serveur WSGI
- Configurez un stockage distant pour les fichiers médias (ex: AWS S3, Cloudinary)

## Liste des bibliothèques utilisées
```
asgiref==3.8.1
attrs==25.1.0
certifi==2025.1.31
charset-normalizer==3.4.1
Django==5.1.5
django-anymail==12.0
django-ckeditor==6.7.2
django-filter==25.1
django-js-asset==3.0.1
djangorestframework==3.15.2
drf-spectacular==0.28.0
drf-yasg==1.21.9
Faker==36.1.1
idna==3.10
inflection==0.5.1
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
Markdown==3.7
packaging==24.2
pillow==11.1.0
pytz==2025.1
PyYAML==6.0.2
referencing==0.36.2
requests==2.32.3
rpds-py==0.23.1
sqlparse==0.5.3
tzdata==2025.1
uritemplate==4.1.1
urllib3==2.3.0
```

## Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier à votre convenance.

---
Développé avec ❤️ par Paul Emmanuel (ZieTech-dev).

# blog_l2_2425
 
