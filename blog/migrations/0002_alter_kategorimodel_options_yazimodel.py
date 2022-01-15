# Generated by Django 4.0 on 2022-01-15 18:30

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorimodel',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.CreateModel(
            name='YaziModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='yazi_resimleri')),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', models.TextField()),
                ('olusturma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('duzenlenme_tarihi', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('kategoriler', models.ManyToManyField(related_name='yazi', to='blog.KategoriModel')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazilar', to='auth.user')),
            ],
            options={
                'verbose_name': 'Yazi',
                'verbose_name_plural': 'Yazilar',
                'db_table': 'Yazi',
            },
        ),
    ]
