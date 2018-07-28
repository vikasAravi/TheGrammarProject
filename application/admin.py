from django.contrib import admin
from .models import Question,AnswerScript
@admin.register(Question)
@admin.register(AnswerScript)

class QuestionAdmin(admin.ModelAdmin):
    pass

class AnswerScriptAdmin(admin.ModelAdmin):
    pass
