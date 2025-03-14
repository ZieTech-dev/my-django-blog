from django import forms
from .models import Article, Categorie, Tag
from django.core.exceptions import ValidationError
from datetime import date
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['titre', 'couverture', 'resume' , 'categorie_id', 'tag_ids','contenu']
        widgets = {
            'titre': forms.TextInput(attrs={
                "type": "text",
                "name": "titre",
                "class": "form-control",
                "id": "titre",
                "placeholder": "titre*"
                }),
            'couverture': forms.FileInput(attrs={
                "name": "couverture",
                "class": "form-control",
                "id": "couverture",
                "placeholder": "couverture*"
                }),
            'tag_ids': forms.SelectMultiple(attrs={
                "name": "tags",
                "class": 'form-control',
                "id": "tags",
                "placeholder": "tags*"
                }),
            'categorie_id': forms.Select(attrs={
                "name": "categorie",
                "class": 'form-control',
                "id": "categorie_id",
                "placeholder": "categorie_id*",
                "title": "categorie"
                
                }),
            'resume': forms.Textarea(attrs={
                "name": "resumé",
                "class": 'form_control',
                "id": "resume",
                "rows":"4",
                "placeholder": "votre resumé...*",
                "title": "tag"
                }),
            'contenu' : forms.CharField(widget=CKEditorWidget()),
        }

    def clean_categorie_id(self):
        """ Vérifie si la catégorie existe, sinon elle est créée. """
        categorie = self.cleaned_data['categorie_id']
        if not Categorie.objects.filter(nom=categorie.nom).exists():
            categorie.save()
        return categorie

    def clean_tag_ids(self):
        """ Vérifie si chaque tag existe, sinon il est créé. """
        tags = self.cleaned_data['tag_ids']
        for tag in tags:
            if not Tag.objects.filter(nom=tag.nom).exists():
                tag.save()
        return tags

    def clean_couverture(self):
        couverture = self.cleaned_data.get('couverture')
        if not couverture:
            raise forms.ValidationError("Veuillez ajouter une image de couverture.")
        return couverture

    def save(self, commit=True):
        """ Définit automatiquement la date de publication et force `est_publie` à False. """
        article = super().save(commit=False)
        article.date_de_publication = date.today()  
        article.est_publie = True 

        if commit:
            article.save()
            self.save_m2m()  

        return article


from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe', 'type':"text"}),
        label="Mot de passe")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Confirme Mot de passe', 'type':"text"}),
        label="Confirmer le mot de passe")
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur', 'type':"text"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'email', 'type':"text"})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data



from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nom d\'utilisateur', 'type':"text"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Mot de passe', 'type':"text"})
    )