from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('post/<int:pk>/', views.detalhe_postagem, name = 'detalhe_post'),
	path('editar_postagem/<int:pk>/', views.editar_postagem, name="edicao_postagem"),
	path('post/new/', views.adicionar_postagem, name = 'adicionar_postagem')
]
