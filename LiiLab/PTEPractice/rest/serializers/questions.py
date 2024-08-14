from rest_framework import serializers
from ...models import QuestionType, SSTQuestion, ROQuestion, RMMCQQuestion

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'name']

class SSTQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSTQuestion
        fields = ['id', 'title','reference_summary', 'time_limit', 'audios', 'question_type']

class ROQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROQuestion
        fields = ['id', 'title', 'paragraphs', 'correct_order', 'question_type']

class RMMCQQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMMCQQuestion
        fields = ['id', 'title', 'passage', 'options', 'correct_options', 'question_type']
