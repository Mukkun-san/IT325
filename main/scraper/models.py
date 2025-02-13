from djongo import models
from django import forms
import django


class Article(models.Model):
    title = models.TextField(blank=False, default="")
    content = models.TextField(blank=False, default="")
    date = models.DateTimeField(auto_now_add=True)


class Distractor(models.Model):
    i = models.IntegerField()
    v = models.TextField(blank=False, default="")

    class Meta:
        abstract = True


class Question(models.Model):
    question = models.TextField(blank=False, default="")
    answer = models.TextField(blank=False, default="")
    distractors = models.ArrayField(model_container=Distractor)

    class Meta:
        abstract = True


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question", "answer")


class Quiz(models.Model):
    questions = models.ArrayField(
        model_container=Question, model_form_class=QuestionForm
    )
