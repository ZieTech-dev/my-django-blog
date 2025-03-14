from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from blog.models import Article,Like,Commentaire
from .forms import ArticleForm,RegisterForm,CustomLoginForm


def index(request):
    articles_list = Article.objects.filter(est_publie=True).order_by("-date_de_publication")
    paginator = Paginator(articles_list, 6)
    
    page = request.GET.get('page',1)
    
    try:
        articles = paginator.get_page(page)
    except InvalidPage:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.get_page(1)

    datas = {
        "articles": articles,
        "active_index": 'active'
    }

    return render(request, 'index.html', datas)

def about(request):
    datas = {
        "active_about": 'active'

    }

    return render(request, 'about.html', datas)


def blog(request):
    articles_list = Article.objects.filter(est_publie=True).order_by("-date_de_publication")
    paginator = Paginator(articles_list, 6)
    
    page = request.GET.get('page',1)
    
    try:
        articles = paginator.get_page(page)
    except InvalidPage:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.get_page(1)

    datas = {
        "articles": articles,
        "active_blog": 'active'
    }

    return render(request, 'blog.html', datas)


def blog_single(request,slug):
    article = Article.objects.get(slug = slug)
    commentaires =Commentaire.objects.filter(article_id=article)
    paginator = Paginator(commentaires, 3)
    
    page = request.GET.get('page',1)
    
    try:
        commentaires = paginator.get_page(page)
    except InvalidPage:
        commentaires = paginator.page(1)
    except EmptyPage:
        commentaires = paginator.get_page(1)

    datas = {
        "article" : article,
        "commentaires" : commentaires
    }

    return render(request, 'blog-single.html', datas)


def contact(request):
    datas = {
        "active_contact": 'active'
    }

    return render(request, 'contact.html', datas)




from django.contrib.auth.decorators import login_required

@login_required
def creer_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur_id = request.user
            article.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = ArticleForm()
        # print(f"{form}")
    return render(request, 'create_article.html', {'form': form, "active_create": 'active','title_boutton':'Créer article'})

@login_required
def dashboard_blog(request):
    articles_list = Article.objects.filter(auteur_id=request.user.id, est_publie=True).order_by("-date_de_publication")
    paginator = Paginator(articles_list, 4)
    
    page = request.GET.get('page',1)
    
    try:
        articles = paginator.get_page(page)
    except InvalidPage:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.get_page(1)

    
    return render(request, 'dashboard_blog.html', {
        "active_dashboard_blog": 'active',
        "articles": articles
    })


@login_required
def dashboard_blog_update(request,slug):
    article = get_object_or_404(Article, slug=slug, auteur_id=request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'create_article.html', {'form': form, "active_create": 'active','title_boutton':'Modifier'})

def dashboard_blog_delete(request, slug):
    article = get_object_or_404(Article, slug=slug, auteur_id=request.user)

    article.est_publie = False
    article.save()

    return redirect('dashboard_blog')



from django.http import JsonResponse
@login_required
def toggle_like(request, slug):
    article = get_object_or_404(Article, slug=slug)
    like, created = Like.objects.get_or_create(user=request.user, article=article)

    if not created:
        like.delete()
        return JsonResponse({'message': 'Like supprimé', 'liked': False})
    
    return JsonResponse({'message': 'Article liké', 'liked': True})

@login_required
def liked_articles(request):
    articles = Article.objects.filter(likes__user=request.user)
    data = [{"id": article.id, "title": article.title, "content": article.content} for article in articles]
    
    return JsonResponse({'liked_articles': data})
