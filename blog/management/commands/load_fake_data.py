from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Categorie, Tag, Article, Commentaire, Like
from django.utils import timezone
import random
from datetime import timedelta

User = get_user_model()

fake = Faker()

class Command(BaseCommand):
    help = 'Charge des données fictives dans la base de données'

    def handle(self, *args, **kwargs):
        Categorie.objects.all().delete()
        User.objects.all().delete()
        Tag.objects.all().delete()
        Article.objects.all().delete()
        Commentaire.objects.all().delete()
        self.create_users(5)
        self.create_categories(80)
        self.create_tags(80)
        self.create_articles(80)
        self.create_comments()
        self.create_likes(100)
        self.stdout.write(self.style.SUCCESS('Données fictives créées avec succès !'))

    def create_users(self, n):
        for _ in range(n):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                photo_profile=fake.image_url(),
                numero_telephone=fake.phone_number(),
                bio=fake.text(),
                rue=fake.street_address(),
                ville=fake.city(),
                code_postal=fake.zipcode(),
                pays=fake.country()
            )
            user.save()

    def create_categories(self, n):
        for _ in range(n):
            categorie = Categorie.objects.create(
                nom=fake.word(),
                description=fake.text()
            )
            categorie.save()

    def create_tags(self, n):
        for _ in range(n):
            tag = Tag.objects.create(
                nom=fake.word()
            )
            tag.save()

    def create_articles(self, n):
        categories = Categorie.objects.all()
        tags = Tag.objects.all()
        users = User.objects.all()
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
                resume=fake.text(),
                contenu=fake.text(),
                auteur_id=random.choice(users),
                categorie_id=random.choice(categories),
                date_de_publication=fake.date_this_year(),
                est_publie=random.choice([True,False]),
            )
            article.slug = fake.slug()
            article.save()

            # Ajouter des tags à l'article
            article.tag_ids.add(*random.sample(list(tags), 3)) 

    def create_comments(self):
        users = User.objects.all()
        articles = Article.objects.all()
        
        for article in articles:
            n = random.randint(0,10)
            for _ in range(n):
                commentaire = Commentaire.objects.create(
                    auteur_id=random.choice(users),
                    article_id=article,
                    contenu=fake.text(),
                )
                commentaire.save()

    def create_likes(self, n):
        """Créer des likes factices."""
        users = User.objects.all()
        articles = Article.objects.all()

        for _ in range(n):
            user = random.choice(users)
            article = random.choice(articles)
            
            # Vérifier si l'utilisateur a déjà aimé cet article
            if not Like.objects.filter(user=user, article=article).exists():
                like = Like.objects.create(
                    user=user,
                    article=article
                )
