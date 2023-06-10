#  hello/views.py

from django.shortcuts import render

def index_view(request):
	return render(request, 'portfolio/index.html')

def projetos_view(request):
	return render(request, 'portfolio/projetos.html')

def contactos_view(request):
	return render(request, 'portfolio/contactos.html')

def sobre_view(request):
	return render(request, 'portfolio/sobre.html')

def jsplayground_view(request):
	return render(request, 'portfolio/jsplayground.html')

def aboutme_view(request):
	return render(request, 'portfolio/aboutme.html')