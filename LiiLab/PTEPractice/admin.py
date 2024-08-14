from django.contrib import admin
from .models import (
    QuestionType, SSTQuestion, ROQuestion, RMMCQQuestion, 
    Answer, SSTScoring, ROScoring, RMMCQScoring, TestSession
)

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(SSTQuestion)
class SSTQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_limit', 'question_type')
    list_filter = ('question_type',)
    search_fields = ('title',)
    readonly_fields = ('audios',)

@admin.register(ROQuestion)
class ROQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question_type')
    list_filter = ('question_type',)
    search_fields = ('title',)
    readonly_fields = ('paragraphs', 'correct_order')

@admin.register(RMMCQQuestion)
class RMMCQQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question_type')
    list_filter = ('question_type',)
    search_fields = ('title',)
    readonly_fields = ('passage', 'options', 'correct_options')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sst_answer', 'ro_answer', 'rmmcq_answer', 'submitted_at', 'score')
    list_filter = ('user',)
    search_fields = ('user__username',)

@admin.register(SSTScoring)
class SSTScoringAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'total_score')
    search_fields = ('answer__user__username',)

@admin.register(ROScoring)
class ROScoringAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'total_score')
    search_fields = ('answer__user__username',)

@admin.register(RMMCQScoring)
class RMMCQScoringAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'total_score')
    search_fields = ('answer__user__username',)

@admin.register(TestSession)
class TestSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'started_at', 'completed_at')
    list_filter = ('user',)
    search_fields = ('user__username',)
