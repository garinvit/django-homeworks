from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
