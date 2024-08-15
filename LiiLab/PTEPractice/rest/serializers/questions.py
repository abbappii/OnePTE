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

    def create(self, validated_data):
        title = validated_data.get('title')
        if SSTQuestion.objects.filter(title=title).exists():
            raise serializers.ValidationError("A question with this title already exists.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        title = validated_data.get('title')
        if title != instance.title and SSTQuestion.objects.filter(title=title).exists():
            raise serializers.ValidationError("A question with this title already exists.")
        return super().update(instance, validated_data)

class ROQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROQuestion
        fields = ['id', 'title', 'paragraphs', 'correct_order', 'question_type']

    def create(self, validated_data):
        title = validated_data.get('title')
        if ROQuestion.objects.filter(title=title).exists():
            raise serializers.ValidationError("A question with this title already exists.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        title = validated_data.get('title')
        if title != instance.title and ROQuestion.objects.filter(title=title).exists():
            raise serializers.ValidationError("A question with this title already exists.")
        return super().update(instance, validated_data)

class RMMCQQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RMMCQQuestion
        fields = ['id', 'title', 'passage', 'options', 'correct_options', 'question_type']

    def create(self, validated_data):
        title = validated_data.get('title')
        if RMMCQQuestion.objects.filter(title=title).exists():
            raise serializers.ValidationError("A question with this title already exists.")
        return super().create(validated_data)
