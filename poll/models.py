from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    def is_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField('选择', max_length=200)
    votes = models.IntegerField('票数', default=0)

    def __str__(self):
        return self.choice_text


