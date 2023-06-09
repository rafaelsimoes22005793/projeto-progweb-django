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

    url = 'https://github.com/rafaelsimoes22005793/projeto-progweb-django'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    div = soup.find('div', class_='plain')
    pre = div.find('pre').text

    cadeiras = pre.split('/')

    lista_cadeiras1 = cadeiras[0].split('\n')[2:-1]
    lista_cadeiras2 = cadeiras[1].split('\n')[2:-1]
    lista_cadeiras3 = cadeiras[2].split('\n')[2:-1]
    
    

    return render(request, 'portfolio/lista_cadeiras.html', {
        'lista1ano': lista_cadeiras1,
        'lista2ano': lista_cadeiras2,
        'lista3ano': lista_cadeiras3,
    })









