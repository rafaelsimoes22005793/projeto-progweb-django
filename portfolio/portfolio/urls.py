from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'


urlpatterns = [
    path('', views.index_view),
    path('admin/', admin.site.urls),
    path('index/', views.index_view, name='index'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('jsplayground/', views.jsplayground_view, name='JSPlayground'),
    path('blog/', views.blog_view, name='blog'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('aboutme/', views.aboutme_view, name='aboutme'),
    path('novo/', views.novo_post_view, name='novo'),
    path('edita/<int:post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_post_view, name='apaga'),
    path('lista_cadeiras/', views.lista_cadeiras_view, name='lista_cadeiras'),
    
]

urlpatterns += static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT)
