# Generated by Django 2.1.5 on 2019-03-17 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190317_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='titulo-del-post', help_text='Se auto-rellena al escribir el Título', max_length=255, unique_for_date='date', verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
    ]
