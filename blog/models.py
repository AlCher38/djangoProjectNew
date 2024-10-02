from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    body = models.TextField(verbose_name="Содержимое",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
