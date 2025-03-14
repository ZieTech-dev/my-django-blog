from django.urls import path,include
from blog import views
# from rest_framework import routers
# from blog.viewsets import ArticleViewSet

# router = routers.DefaultRouter()
# router.register(r'article', ArticleViewSet)

urlpatterns = [
    path("all/", views.blog, name="blog"),
    path("single/<slug:slug>/", views.blog_single, name="blog_single"),
    path('create/', views.creer_article, name='create_article'),
    path('dashboard_blog/', views.dashboard_blog, name='dashboard_blog'),
    path('dashboard_blog/update/<slug:slug>', views.dashboard_blog_update, name='dashboard_blog_update'),
    path('dashboard_blog/delete/<slug:slug>', views.dashboard_blog_delete, name='dashboard_blog_delete'),

    path('like/<slug:slug>', views.toggle_like, name='toggle_like'),
    path('liked-articles', views.liked_articles, name='liked_articles'),
    
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
