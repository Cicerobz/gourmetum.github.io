from django.db import models

# Create your models here.
class Slideshow(models.Model):
	titulo = models.CharField('Titulo inicial', max_length = 100)
	decricao = models.CharField('Descrição', max_length = 200)
	imagem = models.ImageField('Imagem', upload_to= 'slideshow/imagens')

    class Meta:
		verbose_name = "Slideshow"
		verbose_name_plural = "Slideshow"

	def __str__(self):
		return self.titulo


