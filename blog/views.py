from django.shortcuts import render, get_object_or_404
from blog.models import Postagem
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.

def home(request):
	Postagens = Postagem.objects.all().order_by("-data_criacao")
	return render(request, 'home.html', {'Postagens': Postagens})

def detalhe_postagem(request, pk):
	postagem = Postagem.objects.get(pk=pk)
	return render(request, 'detalhe_postagem.html', {'postagem': postagem})

def adicionar_postagem(request):
	if request.method == "POST":
		if form.is_valid():
			#Quando for para salvar
			form = PostForm(request.POST)
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect("home")

	else:
		#Primeiro acesso
		form = PostForm()

	return render(request, 'editar_postagem.html', {'form': form})

def editar_postagem(request, pk):
	postagem = get_object_or_404(Postagem, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=postagem)
		if form.is_valid():
			#Quando for para salvar
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect("home")

	else:
		#Primeiro acesso
		form = PostForm(instance=postagem)

	return render(request, 'editar_postagem.html', {'form': form})