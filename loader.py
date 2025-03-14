#!/usr/bin/env python
import os
import django
import random
from faker import Faker
from django.contrib.auth import get_user_model
from blog.models import Categorie, Tag, Article, Commentaire


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iit.settings')
django.setup()

fake = Faker()
User = get_user_model()

def create_categories(n=5):
    """Créer des catégories factices."""
    categories = []
    for _ in range(n):
        cat = Categorie.objects.create(
            nom=fake.word().capitalize(),
            description=fake.sentence(),
            statut=True
        )
        categories.append(cat)
    return categories

def create_tags(n=30):
    """Créer des tags factices."""
    tags = []
    for _ in range(n):
        tag = Tag.objects.create(
            nom=fake.word().capitalize(),
            statut=True
        )
        tags.append(tag)
    return tags

def create_users(n=5):
    """Créer des utilisateurs factices."""
    users = []
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password=""
        )
        users.append(user)
    return users

def create_articles(n=60, categories=None, users=None, tags=None):
    """Créer des articles factices."""
    articles = []
    list_url_couverture =["articles/blog.jpg",
                          "articles/blog2.jpg",
                          "articles/blog3.jpg",
                          "articles/blog4.jpg",
                          "articles/blog5.jpg",
                          "articles/blog6.png",
                          "articles/blog8.png",
                          "articles/blog9.png",
                          "articles/blog10.png",
                          "articles/blog11.jpg"
                          ]
    for _ in range(n):
        article = Article.objects.create(
            titre=fake.sentence(),
            couverture=random.choice(list_url_couverture),
            resume=fake.paragraph(),
            contenu=fake.text(max_nb_chars=1000),
            auteur_id=random.choice(users),
            categorie_id=random.choice(categories),
            est_publie=random.choice([True, False]),
            date_de_publication=fake.date_this_year(),
            # slug=fake.slug()
        )
        article.tag_ids.set(random.sample(tags, k=random.randint(1, 3)))
        articles.append(article)
    return articles

def create_commentaires(n=20, users=None, articles=None):
    """Créer des commentaires factices."""
    commentaires = []
    for _ in range(n):
        commentaire = Commentaire.objects.create(
            auteur_id=random.choice(users),
            article_id=random.choice(articles),
            contenu=fake.sentence()
        )
        commentaires.append(commentaire)
    return commentaires

def run():
    """Exécute le script de génération de données factices."""
    print("📌 Suppression des anciennes données...")
    Categorie.objects.all().delete()
    Tag.objects.all().delete()
    Article.objects.all().delete()
    Commentaire.objects.all().delete()

    print("✅ Création des nouvelles données...")
    categories = create_categories()
    tags = create_tags()
    # users = create_users()
    users = list(User.objects.all())
    articles = create_articles(categories=categories, users=users, tags=tags)
    create_commentaires(users=users, articles=articles)

    print("🎉 Données factices insérées avec succès !")

# Exécuter le script
if __name__ == "__main__":
    run()
