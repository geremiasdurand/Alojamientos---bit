from django.db import models
import datetime

# Create your models here.
class Comment(models.Model):
    #tengo que agregarlo  en la app de residencias
    #post = models.ForeignKey("residencia.id", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("usuario.student", on_delete=models.CASCADE, related_name="user")
    text = models.CharField(max_length=280)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    #si es que podemos hacer lo de aprovados
    #approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text
