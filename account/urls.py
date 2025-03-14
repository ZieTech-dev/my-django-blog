from django.urls import path
from .views import home,register,sing_in,log_out,forgot_password,update_password,active_compte

urlpatterns = [
    path('register', register,name='register'),
    path('sing_in', sing_in,name='sing_in'),
    path('log_out', log_out,name='log_out'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password/<str:token>/<str:user_id>', update_password, name='update_password'),
    path('update-password/<str:token>/<str:user_id>/active', active_compte, name='active_compte'),
]
