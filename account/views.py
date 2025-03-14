from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.validators import validate_email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
import codecs
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.
User = get_user_model()
#page acceuille
@login_required(login_url='sing_in')
def home(request):
    data={
        'home_active' :'active',
    }
    return render(request,"account/home.html",data)

# page inscription
def register(request):
    error = False
    message=''
    if request.method == 'POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        print(f"mon :{name} , email:{email} , mdp1:{password1}, mdp2:{password2}")
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password1 != password2:
                error = True
                message = "Les deux mot de passe ne sont pas les même 🤦!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password1
            user.set_password(user.password)
            user.is_active = False
            user.save()
            if user:
                print("processing forgot password")
                token = default_token_generator.make_token(user)
                user_id = urlsafe_base64_encode(force_bytes(user.id))
                domaine = request.META['HTTP_HOST']
                html_text = render_to_string("account/email.html",{
                    "token":token,
                    "user_id":user_id,
                    "active":False,
                    "titre":"Activation de compte",
                    "message":"Si vous activer votre compte et finaliser l'inscription, utilisez le lien ci-dessous pour commencer :",
                    "texte_boutton":"Activer mon compte",
                    "curent_site": f"http://{domaine}",
                })

                msg = EmailMessage(
                    "Modification de mot de pass!",
                    html_text,
                    "paulemmanuelouattara@gmail.com",
                    ["ouatpaulo@gmail.com",email],
                )

                msg.content_subtype = 'html'
                msg.send()
                
                message = "processing forgot password"
                success = True
            else:
                print("l'utilisateur n'a pas ete sauvegarder")
                error = True
                message = "l'utilisateur n'a pas ete sauvegarder"

            return redirect('sing_in')

    data={
    'register_active' :'active',
    'message' : message,
    'error': error,
    }
    
    return render(request,"account/register.html",data)


def sing_in(request):
    error = False
    message=''
    if request.method == 'POST':
        email =request.POST.get('email',None)
        password = request.POST.get('password',None)
        print(f"Email:{email} , password:{password}")
        user =User.objects.filter(email=email).first()
        if user.is_active==True:
            if user:
                auth_user = authenticate(username=user.username, password=password)
                if auth_user:
                    login(request, auth_user)
                    return redirect('index')
                else:
                    error = True
                    message = "mot de pass incorrecte"
                    print("mot de pass incorrecte")
            else:
                error = True
                message = "L'utilisateur n'existe pas !"
                print("L'utilisateur n'existe pas !")
        else:
            error = True
            message = "votre compte n'est pas actif,verifier vos mail"
            print("votre compte n'est pas actif,verifier vos mail")
    
    data={
    'sing_in_active' :'active',
    'message' : message,
    'error': error,
    }
    return render(request,"account/login.html",data)


def log_out(request):
    logout(request)
    return redirect('sing_in')


def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            print("processing forgot password")
            token = default_token_generator.make_token(user)
            user_id = urlsafe_base64_encode(force_bytes(user.id))
            domaine = request.META['HTTP_HOST']
            html_text = render_to_string("account/email.html",{
                "token":token,
                "user_id":user_id,
                "active":True,
                "texte_boutton":"Reset Your Password",
                "titre":"Forget password ?",
                "message":"Si vous avez perdu votre mot de passe ou souhaitez le réinitialiser, utilisez le lien ci-dessous pour commencer :",
                "curent_site": f"http://{domaine}",
            })

            msg = EmailMessage(
                "Modification de mot de pass!",
                html_text,
                "paulemmanuelouattara@gmail.com",
                ["ouatpaulo@gmail.com",email],
            )

            msg.content_subtype = 'html'
            msg.send()
            
            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"
    
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "account/forgot_password.html", context)

def active_compte(request, token, user_id):
    print(f"Token: {token}, User ID: {user_id}")
    user = None
    message = ""
    success = False
    error = False

    try:
        decode_user_id = int(urlsafe_base64_decode(user_id).decode('utf-8'))
        user = User.objects.filter(id=decode_user_id).first()
        

        if user is None:
            message = "Utilisateur introuvable."
            error = True
        elif not default_token_generator.check_token(user, token):
            message = "Lien de réinitialisation invalide ou expiré."
            error = True
        else:
            user.is_active=True
            user.save()
            message = "votre compte est actif "
            success = True
    except (ValueError, TypeError, OverflowError):
        message = "Lien de réinitialisation invalide."
        error = True

    context = {
        'success': success,
        'message': message,
        'user': user,
        'error': error,
    }

    return render(request, "account/active_password.html", context)



def update_password(request, token, user_id):
    print(f"Token: {token}, User ID: {user_id}")
    user = None
    message = ""
    success = False
    error = False

    try:
        decode_user_id = int(urlsafe_base64_decode(user_id).decode('utf-8'))
        user = User.objects.filter(id=decode_user_id).first()
        

        if user is None:
            message = "Utilisateur introuvable."
            error = True
        elif not default_token_generator.check_token(user, token):
            message = "Lien de réinitialisation invalide ou expiré."
            error = True
        else:
            if request.method == "POST":
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')

                if password1 and password2:
                    if password1 == password2:
                        try:
                            validate_password(password1, user)
                            user.set_password(password1)
                            user.is_active=True
                            user.save()
                            
                            success = True
                            message = "Votre mot de passe a été modifié avec succès !"
                        except ValidationError as e:
                            error = True
                            message = " ".join(e.messages)
                    else:
                        error = True
                        message = "Les mots de passe ne correspondent pas."
                else:
                    error = True
                    message = "Veuillez remplir les deux champs de mot de passe."

    except (ValueError, TypeError, OverflowError):
        message = "Lien de réinitialisation invalide."
        error = True

    context = {
        'success': success,
        'message': message,
        'user': user,
        'error': error,
    }

    return render(request, "account/update_password.html", context)

# def update_password(request, token, user_id):
#     print(f"Token: {token}, User ID: {user_id}")
#     user = None
#     message = ""
#     success = False
#     error = False

#     try:
#         decode_user_id = int(urlsafe_base64_decode(user_id).decode('utf-8'))
#         user = User.objects.filter(id=decode_user_id).first()

#         if user is None:
#             message = "Utilisateur introuvable."
#         elif not default_token_generator.check_token(user, token):
#             message = "Lien de réinitialisation invalide ou expiré."
#         else:
#             success = True
#             password1 = request.POST.get('password1',None)
#             password2 = request.POST.get('password2',None)
#             if password1 == password2:
#                 try:
#                     validate_password(password1,user)
#                     user.set_password(password1)
#                     user.save()
#                     success=True
#                     message="Bravo"
#                 except ValidationError as e:
#                     error = True
#                     message=str(e)
#             message = "Vous pouvez maintenant modifier votre mot de passe."

#     except (ValueError, TypeError, OverflowError):
#         message = "Lien de réinitialisation invalide."

#     context = {
#         'success': success,
#         'message': message,
#         'user': user,
#         'error': error,
#     }

#     return render(request, "account/update_password.html", context)
