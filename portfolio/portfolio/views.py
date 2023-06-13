from django.shortcuts import get_object_or_404, render,redirect
from .models import Post
from .forms import PostForm
import requests
from bs4 import BeautifulSoup



def index_view(request):
	return render(request, 'portfolio/index.html')

def projetos_view(request):
	return render(request, 'portfolio/projetos.html')

def contactos_view(request):
	return render(request, 'portfolio/contactos.html')

def sobre_view(request):
	return render(request, 'portfolio/sobre.html')

def jsplayground_view(request):
	return render(request, 'portfolio/JSPlayground.html')

def blog_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/blog.html', context)
    

def aboutme_view(request):
	return render(request, 'portfolio/aboutme.html')

def sobre_view(request):
	return render(request, 'portfolio/sobre.html')


def novo_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm()

    return render(request, 'portfolio/novo.html', {'form': form})


def edita_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = PostForm(instance=post)

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('blog')

def lista_cadeiras_view(request):

    lista_1ano = []
    lista_2ano = []
    lista_3ano = []

    url = 'https://informatica.ulusofona.pt/cursos/licenciaturas/engenharia-informatica/lei-plano/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tabelaSite = soup.find_all('table')[:3]

    for tableBody in tabelaSite[0].find_all('tbody'):
        for linha in tableBody.find_all('tr'):
            dados = linha.find('td').text
            lista_1ano.append(dados)

    for tableBody in tabelaSite[1].find_all('tbody'):
        for linha in tableBody.find_all('tr'):
            dados = linha.find('td').text
            lista_2ano.append(dados)

    for tableBody in tabelaSite[2].find_all('tbody'):
        for linha in tableBody.find_all('tr'):
            dados = linha.find('td').text
            lista_3ano.append(dados)

    return render(request, 'portfolio/lista_cadeiras.html',{
            'lista1ano': lista_1ano,
            'lista2ano': lista_2ano,
            'lista3ano': lista_3ano
    })



