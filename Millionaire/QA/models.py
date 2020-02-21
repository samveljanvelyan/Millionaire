from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MultipleChoiceQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000, null=True)
    rank = models.IntegerField(default=5, choices=[(5, 5), (10, 10), (15, 15), (20, 20)],
                               null=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(
        MultipleChoiceQuestion, on_delete=models.CASCADE, to_field='id', null=True
    )
    first_answer = models.CharField(max_length=1000, default='first answer', null=True)
    second_answer = models.CharField(max_length=1000, default='second answer', null=True)
    third_answer = models.CharField(max_length=1000, default='third_answer', null=True)
    fourth_answer = models.CharField(max_length=1000, default='fourth answer', null=True)
    correct_answer = models.CharField(max_length=1000, default=None, null=True)

    def __str__(self):
        return (f'{self.first_answer}\n{self.second_answer}\n'
                f'{self.third_answer}\n{self.fourth_answer}')


class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
