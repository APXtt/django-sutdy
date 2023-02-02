from django.contrib import admin

# Register your models here.

from . models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): # 관리자 페이지에서 그룹화 시킨 것
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
