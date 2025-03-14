from blog.models import Article, Categorie, Tag
from django.utils import timezone

# Sélectionner une catégorie et un tag
categorie = Categorie.objects.get(nom="Technologie")
tag = Tag.objects.get(nom="Python")


from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(pk=2)

# Créer un nouvel article
article = Article.objects.create(
    titre="Introduction à Python",
    couverture="path_to_image",  # Remplacer par un chemin d'image valide
    resume="Un article sur les bases de Python.",
    contenu="Le contenu détaillé de l'article",
    auteur_id=2,
    categorie_id=categorie,
    date_de_publicatio=timezone.now().date(),
)

# Ajouter des tags à l'article
article.tag_ids.add(tag)

# Afficher l'article créé
print(article)





from blog.models import Commentaire

# Sélectionner un article
article = Article.objects.get(titre="Introduction à Python")

# Créer un commentaire pour l'article
commentaire = Commentaire.objects.create(
    auteur_id=user,
    article_id=article,
    contenu="C'est un excellent article sur Python, merci pour le partage !"
)

# Afficher le commentaire créé
print(commentaire)
