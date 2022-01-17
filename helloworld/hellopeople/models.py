from django.db import models


class Name(models.Model):
    name = models.CharField('Ім\'я', max_length=65, primary_key=True)

    def __str__(self):
        return self.name
