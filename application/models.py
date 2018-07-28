from django.db import models
import datetime# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length = 256)

    def __str__(self):
        return "{content}".format(content = self.question_text)

class AnswerScript(models.Model):
    answer_text = models.TextField()
    

    def __str__self(self):
        return "{content}".format(content= self.answer_text)