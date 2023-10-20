from django.db import models

import anketa.models


# Create your models here.

#class Gragdanin(User):
#    mydata = models.TextField(max_length=50, verbose_name = '')

class MeTest(models.Model):
    title = models.TextField(max_length=50, verbose_name = 'НАЗВАНИЕ')
    professia = models.ForeignKey(anketa.models.Professia, on_delete=models.PROTECT, verbose_name='Профессия')#


    class Meta:
        ordering = ["-title"]
        verbose_name = 'Мой новый класс'
        verbose_name_plural = 'Мой новый класс'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in MeTest._meta.fields]
