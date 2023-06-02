from django.db import models

class Movie(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    director = models.ForeignKey('Director', models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table ="movies"


class Director(models.Model):

    name = models.CharField(null=False, blank=False, max_length=128)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "directors"



