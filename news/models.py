from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    STATUS_CHOICES = (
        ('unpublish', 'Unpublish',),
        ('publish', 'Publish'),
    )
    image_news = models.ImageField(verbose_name='Image', upload_to='images/news', blank=False, null=True)
    # image_news2 = models.ImageField(verbose_name='Image2', upload_to='images/news', blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=80, blank=False, unique=True)
    body = models.TextField(verbose_name='Content', blank=False)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='unpublish')
    publish = models.DateField()
    author = models.CharField(verbose_name='Author', max_length=50, blank=False)
    created = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail",
                       kwargs={"id": self.id}
                       )

    def image1(self):
        return "<img src='{}' width=50px>" .format(self.image_news.url)
    image1.allow_tags=True

    # def image2(self):
    #     return "<img src='{}' width=50px>" .format(self.image_news2.url)
    # image2.allow_tags=True

