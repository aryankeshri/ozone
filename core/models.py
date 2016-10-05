from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

from django.core.validators import RegexValidator

age_validation = RegexValidator(regex=r'^0*[1-9][0-9]*$', message='Age Integer only.')
phone_validation = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Contact number must be entered in the format: '+999999999'.")

class Join(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200, blank=False)
    age = models.CharField(verbose_name='Age', max_length=2, blank=False, validators=[age_validation])
    city = models.CharField(verbose_name='City', max_length=100, blank=False)
    contact = models.CharField(verbose_name='Contact', max_length=16, blank=False, validators=[phone_validation])
    creation = models.DateTimeField(blank=False,auto_now_add=True)

    class Meta:
        unique_together = ("name", "contact")

    def __str__(self):
        return self.name


class PhotoDay(models.Model):
    STATUS_CHOICES = (
        ('unpublish', 'Unpublish',),
        ('publish', 'Publish'),
    )
    image = models.ImageField(upload_to='images/photo-of-day', blank=False, verbose_name='Image', default=False)
    title = models.CharField(verbose_name='Title', max_length=100, blank=False, unique=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='unpublish',
                              verbose_name='Publish/Unpublish')

    def __str__(self):
        return self.title

    def image1(self):
        return "<img src='{}' width=50px>" .format(self.image.url)
    image1.allow_tags=True


class Event(models.Model):
    STATUS_CHOICES = (
        ('unpublish', 'Unpublish',),
        ('publish', 'Publish'),
    )
    image = models.ImageField(upload_to='images/events', blank=False, verbose_name='Image', default=None)
    title = models.CharField(verbose_name='Title', max_length=100, blank=False)
    body = models.TextField(verbose_name='Discription', blank=False)
    date = models.DateField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='unpublish',
                              verbose_name='Publish/Unpublish')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def image1(self):
        return "<img src='{}' width=50px>" .format(self.image.url)
    image1.allow_tags=True


class Ofctv(models.Model):
    TYPE_CHOICES = (
        ('all', 'all',),
        ('i-league', 'i-league'),
        ('champions-league', 'champions-league'),
        ('interview', 'interview'),
        ('documentary', 'documentary'),
    )
    video = EmbedVideoField()
    title = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    type = models.CharField(max_length=20,
                              choices=TYPE_CHOICES,
                              default='all',
                              verbose_name='data-cat')


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title



