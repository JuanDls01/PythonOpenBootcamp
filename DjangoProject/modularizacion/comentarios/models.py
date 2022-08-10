from django.db import models

# Create your models here.


class Comment(models.Model):
    '''Columnas: name, score, text'''

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    text = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.name
