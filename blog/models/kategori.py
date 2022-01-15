from django.db import models
from autoslug import AutoSlugField


class KategoriModel(models.Model):
    isim = models.CharField(max_length=50, null=False, blank=False)
    slug = AutoSlugField(unique=True, populate_from='isim')

    class Meta:
        db_table = 'kategori'
