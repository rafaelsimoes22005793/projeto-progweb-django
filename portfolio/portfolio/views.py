from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm



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
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog')
    context = {'form': form}
    return render(request, 'portfolio/novo.html', context)

def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('blog')

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('blog')


