from django.db import models
from django.contrib.auth import get_user_model
from .choices import QuestionTypes
from common.models import BaseModelWithUID

User = get_user_model()

class QuestionType(BaseModelWithUID):
    name = models.CharField(
        max_length=10,
        choices=QuestionTypes.choices,
        unique=True
    )
    def __str__(self):
        return self.name

class SSTQuestion(BaseModelWithUID):
    title = models.CharField(max_length=255)
    time_limit = models.IntegerField(help_text="Time limit in seconds")
    audios = models.JSONField(help_text="JSON format: [{'speaker': 'name', 'audio_file': 'path'}]")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    reference_summary = models.TextField(
        help_text="This will contain the key points expected in the student's summary."
    )

    def __str__(self):
        return self.title


class ROQuestion(BaseModelWithUID):
    title = models.CharField(max_length=255)
    paragraphs = models.JSONField(help_text="List of paragraphs in random order")
    correct_order = models.JSONField(help_text="List of paragraphs in correct order")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RMMCQQuestion(BaseModelWithUID):
    title = models.CharField(max_length=255)
    passage = models.TextField()
    options = models.JSONField(help_text="List of options")
    correct_options = models.JSONField(help_text="List of correct options")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answer(BaseModelWithUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sst_question = models.ForeignKey(SSTQuestion, on_delete=models.CASCADE, null=True, blank=True)
    ro_question = models.ForeignKey(ROQuestion, on_delete=models.CASCADE, null=True, blank=True)
    rmmcq_question = models.ForeignKey(RMMCQQuestion, on_delete=models.CASCADE, null=True, blank=True)
    sst_answer = models.TextField(null=True, blank=True)
    ro_answer = models.JSONField(null=True, blank=True, help_text="Submitted paragraph order")
    rmmcq_answer = models.JSONField(null=True, blank=True, help_text="Submitted options")
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True, blank=True, help_text="Total score for the answer")

    def __str__(self):
        return f"Answer by {self.user}"


class SSTScoring(BaseModelWithUID):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    content_score = models.IntegerField()
    form_score = models.IntegerField()
    grammar_score = models.IntegerField()
    vocabulary_score = models.IntegerField()
    spelling_score = models.IntegerField()
    total_score = models.IntegerField()

    def __str__(self):
        return f"Scoring for {self.answer}"


class ROScoring(BaseModelWithUID):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    correct_pairs = models.IntegerField(help_text="Number of correctly ordered adjacent pairs")
    total_score = models.IntegerField()

    def __str__(self):
        return f"Scoring for {self.answer}"


class RMMCQScoring(BaseModelWithUID):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    correct_choices = models.IntegerField(help_text="Number of correct choices selected")
    incorrect_choices = models.IntegerField(help_text="Number of incorrect choices selected")
    total_score = models.IntegerField()

    def __str__(self):
        return f"Scoring for {self.answer}"


class TestSession(BaseModelWithUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sst_questions = models.ManyToManyField(SSTQuestion, blank=True)
    ro_questions = models.ManyToManyField(ROQuestion, blank=True)
    rmmcq_questions = models.ManyToManyField(RMMCQQuestion, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.user} started at {self.started_at}"
