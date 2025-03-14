from rest_framework import viewsets
from blog.models import Article,Categorie,Tag,Commentaire,Like
from blog.serializers import ArticleSerializer,CategorieSerializer,TagSerializer,CommentaireSerializer,LikeSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    permission_classes = [IsAuthenticated]
   
    
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
    permission_classes = [IsAuthenticated]
    
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes = [IsAuthenticated]
    
    
class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    
    permission_classes = [IsAuthenticated]


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    permission_classes = [IsAuthenticated]

# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# class ArticleViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet permettant de gérer les articles (CRUD).
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticated]

#     @swagger_auto_schema(
#         operation_description="Récupérer un article par son ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,  # Indique que l'id est dans l'URL
#                 description="L'identifiant de l'article à récupérer",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={200: ArticleSerializer()}
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)



# class ArticleViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet permettant de gérer les articles (CRUD).
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticated]

#     # 📌 GET /api/articles/{id}/ (récupérer un article spécifique)
#     @swagger_auto_schema(
#         operation_description="Récupérer un article par son ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à récupérer",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={200: ArticleSerializer()}
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     # 📌 PUT /api/articles/{id}/ (mise à jour complète)
#     @swagger_auto_schema(
#         operation_description="Mettre à jour complètement un article",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à mettre à jour",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={200: ArticleSerializer()}
#     )
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # 📌 PATCH /api/articles/{id}/ (mise à jour partielle)
#     @swagger_auto_schema(
#         operation_description="Modifier partiellement un article",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à modifier",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={200: ArticleSerializer()}
#     )
#     def partial_update(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)

#     # 📌 DELETE /api/articles/{id}/ (supprimer un article)
#     @swagger_auto_schema(
#         operation_description="Supprimer un article par son ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à supprimer",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={204: "L'article a été supprimé avec succès."}
#     )
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)



# class ArticleViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet permettant de gérer les articles (CRUD).
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         """
#         Utiliser un serializer avec tous les champs visibles pour PUT/PATCH.
#         """
#         if self.action in ['update', 'partial_update']:
#             class FullArticleSerializer(ArticleSerializer):
#                 class Meta(ArticleSerializer.Meta):
#                     extra_kwargs = {field: {'required': False} for field in ArticleSerializer.Meta.fields}
            
#             return FullArticleSerializer

#         return ArticleSerializer

#     # 📌 GET /api/articles/{id}/ (récupérer un article spécifique)
#     @swagger_auto_schema(
#         operation_description="Récupérer un article par son ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à récupérer",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={200: ArticleSerializer()}
#     )
#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     # 📌 PUT /api/articles/{id}/ (mise à jour complète)
#     @swagger_auto_schema(
#         operation_description="Mettre à jour complètement un article avec tous les champs",
#         request_body=ArticleSerializer,
#         responses={200: ArticleSerializer()}
#     )
#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     # 📌 PATCH /api/articles/{id}/ (mise à jour partielle)
#     @swagger_auto_schema(
#         operation_description="Modifier partiellement un article avec tous les champs disponibles",
#         request_body=ArticleSerializer,
#         responses={200: ArticleSerializer()}
#     )
#     def partial_update(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)

#     # 📌 DELETE /api/articles/{id}/ (supprimer un article)
#     @swagger_auto_schema(
#         operation_description="Supprimer un article par son ID",
#         manual_parameters=[
#             openapi.Parameter(
#                 'id',
#                 openapi.IN_PATH,
#                 description="L'identifiant de l'article à supprimer",
#                 type=openapi.TYPE_INTEGER,
#                 required=True
#             )
#         ],
#         responses={204: "L'article a été supprimé avec succès."}
#     )
#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

