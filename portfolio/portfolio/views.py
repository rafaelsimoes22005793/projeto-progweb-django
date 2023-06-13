from django.shortcuts import get_object_or_404, render,redirect
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


