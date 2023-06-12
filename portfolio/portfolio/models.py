from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=500, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

     