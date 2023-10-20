from django.db import models

# Create your models here.

#class Gragdanin(User):
#    mydata = models.TextField(max_length=50, verbose_name = '')

class MeTest(models.Model):
    title = models.TextFile(max_length=50, verbose_name = 'НАЗВАНИЕ')
    professia = models.ForeignKey(on_delta=models.PROTECT, verbase_name='Профессия')#


    class Meta:
        ordering = ["-title"]
        verbose_name = 'Мой новый класс'
        verbose_name_plural = 'Мой новый класс'

    def __str__(self):
        return [(field.name, field.value_to_string(self))
                for field in MeTest._meta.fields]
