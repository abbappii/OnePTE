from rest_framework import serializers
from ...models import SSTScoring, ROScoring, RMMCQScoring, TestSession


class SSTScoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSTScoring
        fields = ['id', 'answer', 'content_score', 'form_score', 'grammar_score', 'vocabulary_score', 'spelling_score', 'total_score']

class ROScoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROScoring
        fields = ['id', 'answer', 'correct_pairs', 'total_score']

class RMMCQScoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMMCQScoring
        fields = ['id', 'answer', 'correct_choices', 'incorrect_choices', 'total_score']

class TestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSession
        fields = ['id', 'user', 'questions', 'started_at', 'completed_at']
