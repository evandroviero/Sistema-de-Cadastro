from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view resposanvel, nome de referencia
    path('', views.home, name= 'home'),
    path('usuarios/', views.usuario, name='listagem_usuarios')
]
