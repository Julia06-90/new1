from django.db import models
from django.db.models.signals import post_save, pre_delete
from datetime import datetime
from django.dispatch import receiver
from django.contrib.auth.models import User, UserManager

class Chapter(models.Model):
    theme = models.CharField(max_length=200)
    article_count = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return self.theme

class Article(models.Model):
    article_text = models.TextField()
    time = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter,related_name='actual')
#    old_chapter = models.ForeignKey(Chapter,related_name='old')

    def __unicode__(self):
        return self.title

    def foo(self):
        return 'foo'


class Commentary(models.Model):
    comment_text = models.TextField()
    comment_time = models.DateTimeField(default=datetime.now)
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.comment_text





@receiver(post_save, sender=Article)
def handle_new_article_created(sender, instance, *args, **kwargs):
    if kwargs['created']:
        instance.chapter.article_count += 1
        instance.chapter.save()

@receiver(pre_delete, sender=Article)
def handle_new_article_deleted(sender, instance, *args, **kwargs):
    instance.chapter.article_count -= 1
    instance.chapter.save()