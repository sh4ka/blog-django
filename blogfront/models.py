from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextUploadingField()
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
