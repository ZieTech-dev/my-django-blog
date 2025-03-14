
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.views import index,about,contact
from django.conf.urls.static import static
# Importation de rest_framework
from rest_framework import routers
from blog.viewsets import ArticleViewSet,CategorieViewSet,TagViewSet,CommentaireViewSet,LikeViewSet
# Importation de drf_yasg
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path


# Configuration de drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Documentation de l'API du blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="paulEmmanuelouattara@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
    # permission_classes=(permissions.AllowAny,),
)

@method_decorator(login_required, name='dispatch')
def protected_swagger_view(request, *args, **kwargs):
    return schema_view.with_ui('swagger', cache_timeout=0)(request, *args, **kwargs)


router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'Categories', CategorieViewSet)
router.register(r'Tags', TagViewSet)
router.register(r'Commentaires', CommentaireViewSet)
router.register(r'Likes', LikeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
    
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Génération OpenAPI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),  # Interface Swagger

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
