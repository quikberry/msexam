from django.db import models
from django.contrib.auth.models import User

class smexam(models.Model):
    title = models.CharField("Название экзамена", max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    exam_date = models.DateField("Дата проведения экзамена")
    image = models.ImageField("Файл экзамена (изображение)", upload_to='exam_images/')
    students = models.ManyToManyField(User, verbose_name="Участники экзамена")
    is_public = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return self.title