from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

TITLE = 100
TEXT = 150000


class Post(models.Model):

    slug = models.SlugField(
        _('slug'), max_length=255,
        unique_for_date='date',
        default='titulo-del-post',
        help_text=_("Se auto-rellena al escribir el Título")
    )

    title = models.CharField(max_length=TITLE)
    subtitle = models.CharField(max_length=TITLE, default='')
    intro = HTMLField(max_length=TEXT, default='', blank=True)
    body = HTMLField(max_length=TEXT, default='', blank=True)
    date = models.DateTimeField(
        _('Fecha de publicacion'),
        db_index=True, default=timezone.now,
    )
    main_pic = models.ImageField(upload_to='img/post/')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + " - " + self.title

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        publication_date = self.date
        if timezone.is_aware(publication_date):
            publication_date = timezone.localtime(publication_date)
        return reverse('blog:single', kwargs={
            'year': publication_date.strftime('%Y'),
            'month': publication_date.strftime('%m'),
            'day': publication_date.strftime('%d'),
            'slug': self.slug})

    def get_url(self):
        pub_date = self.date
        return pub_date.strftime('%Y') + '/' + pub_date.strftime('%m') + '/' + pub_date.strftime('%d') + '/' + self.slug


class Imagen(models.Model):
    imgFile = models.ImageField(upload_to='img/')
