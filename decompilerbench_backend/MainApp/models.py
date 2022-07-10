from django.db import models

# Create your models here.

class InferenceModel(models.Model):
    filename = models.CharField(name="filename", verbose_name="Название файла для оценки из папки media", max_length=1024)
    result = models.CharField(name="result", verbose_name="Результат распознавания текста", max_length=4096)
    
    def __str__(self):
        return '{name} => result : {result}'.format(name=self.name,result=self.result)