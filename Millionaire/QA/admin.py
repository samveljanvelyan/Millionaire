from django.contrib import admin

from .models import MultipleChoiceQuestion, QuizTaker, Answer

# Register your models here.
models = [MultipleChoiceQuestion, QuizTaker, Answer]
admin.site.register(models)
