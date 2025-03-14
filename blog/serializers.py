from rest_framework import serializers
from blog.models import Article,Categorie,Tag,Commentaire,Like



class ArticleSerializer(serializers.ModelSerializer):
    couverture = serializers.ImageField(required=False)
    categorie = serializers.SerializerMethodField()
    auteur = serializers.SerializerMethodField()  

    class Meta:
        model = Article
        fields = [
            'titre',
            'couverture',
            'resume',
            'contenu',
            'auteur',  
            'categorie',
            'tag_ids',
            'est_publie',
            'slug',
            'created_at'
        ]
        depth = 1

    def get_categorie(self, obj):
        if obj.categorie_id:
            return {"nom": obj.categorie_id.nom}  
        return None

    def get_auteur(self, obj):
        """Retourne seulement le username de l'auteur."""
        return obj.auteur_id.username if obj.auteur_id else None



class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__'
        depth = 1


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1


class CommentaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentaire
        fields = '__all__'
        depth = 2


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        depth = 2
