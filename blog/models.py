from django.conf import settings
from django.utils import timezone
from django.db import models
from django.urls import reverse
from transliterate import translit



class SubjectPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True, null=True)
    keywords = models.TextField(max_length=200, blank=True, null=True)
    text = models.TextField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'url': self.url})

    # Доступно как поле за счет декоратора property
    @property
    def absolute_url(self):
        return reverse('subject_detail', kwargs={'url': self.url})

    @property
    def subject(self):

        return \
        {
            "title" : self.title,
            "url" : self.absolute_url
        }

    def save(self, *args, **kwargs):
        url = translit(self.title, 'ru', reversed=True)
        self.url = url.replace(" ", "_")
        super(SubjectPost, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='published_date', blank=True, null=True)
    subject = models.ForeignKey('SubjectPost', on_delete=models.CASCADE, related_name='result')
    description = models.TextField(max_length=200, blank=True, null=True)
    keywords = models.TextField(max_length=200, blank=True, null=True)
    text = models.TextField()
    LOAN_STATUS = (
        ('y', 'Опубликовать'),
        ('n', 'Опубликовать позже'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='y', help_text='Публикация?')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_short_text(self):
        return self.text[:900]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])

    def save(self, *args, **kwargs):
        slug = translit(self.title, 'ru', reversed=True)
        self.slug = slug.replace(" ", "_")
        super(Post, self).save(*args, **kwargs)
