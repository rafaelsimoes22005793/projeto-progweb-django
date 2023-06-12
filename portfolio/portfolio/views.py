from django.shortcuts import render, redirect
from .models import Post


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


def home_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'tarefas/home.html', context)



    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('posts:home')

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)


