from django.contrib import admin
from blog.models import Categorie, Tag, Article, Commentaire
from ckeditor.widgets import CKEditorWidget
from django.db import models


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Infos', {'fields': ['nom', 'description']}),
        ('Standards', {'fields': ['statut']})
    ]

    actions = ('active', 'desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'


class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at')
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'get_auteur', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['titre']
    list_filter = ('statut', 'auteur_id')
    search_fields = ('titre', 'contenu', 'auteur_id__username')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10

    fieldsets = [
        ('Informations principales', {'fields': ['titre', 'contenu', 'auteur_id']}),
        ('Catégorisation', {'fields': ['categorie_id', 'tag_ids']}),
        ('Publication', {'fields': ['est_publie', 'date_de_publication']}),
        ('Standards', {'fields': ['statut']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}  
    }

    actions = ('publier', 'depublier')

    def publier(self, request, queryset):
        queryset.update(est_publie=True)
        self.message_user(request, 'Les articles sélectionnés ont été publiés')
    publier.short_description = 'Publier'

    def depublier(self, request, queryset):
        queryset.update(est_publie=False)
        self.message_user(request, 'Les articles sélectionnés ont été dépubliés')
    depublier.short_description = 'Dépublier'

    def get_auteur(self, obj):
        return obj.auteur_id.username if obj.auteur_id else "Anonyme"
    get_auteur.admin_order_field = 'auteur_id'
    get_auteur.short_description = 'Auteur'




class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('get_auteur', 'get_article', 'statut', 'created_at')
    list_display_links = ['get_auteur']
    list_filter = ('statut', 'article_id')
    search_fields = ('auteur_id__username', 'contenu')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10

    fieldsets = [
        ('Informations', {'fields': ['auteur_id', 'article_id', 'contenu']}),
        ('Modération', {'fields': ['statut']})
    ]

    actions = ('approuver', 'rejeter')

    def approuver(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Les commentaires sélectionnés ont été approuvés')
    approuver.short_description = 'Approuver'

    def rejeter(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'Les commentaires sélectionnés ont été rejetés')
    rejeter.short_description = 'Rejeter'

    def get_auteur(self, obj):
        return obj.auteur_id.username if obj.auteur_id else "Anonyme"
    get_auteur.admin_order_field = 'auteur_id'
    get_auteur.short_description = 'Auteur'

    def get_article(self, obj):
        return obj.article_id.titre if obj.article_id else "Sans article"
    get_article.admin_order_field = 'article_id'
    get_article.short_description = 'Article'


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
