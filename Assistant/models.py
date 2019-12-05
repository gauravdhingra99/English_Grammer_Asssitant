from django.contrib.postgres.fields import JSONField
from django.db import models

class Sentence(models.Model):
    query = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.query