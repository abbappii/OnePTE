from rest_framework import serializers
from ...models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'sst_question',
            'ro_question',
            'rmmcq_question',
            'sst_answer',
            'ro_answer',
            'rmmcq_answer',
            'submitted_at',
            'score'
        ]
        read_only_fields = ["user","score"]

    def validate(self, data):
        question_fields = ['sst_question', 'ro_question', 'rmmcq_question']
        answer_fields = ['sst_answer', 'ro_answer', 'rmmcq_answer']

        provided_question = [field for field in question_fields if data.get(field)]
        provided_answer = [field for field in answer_fields if data.get(field)]

        if len(provided_question) > 1 or len(provided_answer) > 1:
            raise serializers.ValidationError("Only one question type and its corresponding answer should be provided.")

        if len(provided_question) == 0 or len(provided_answer) == 0:
            raise serializers.ValidationError("A question and its corresponding answer must be provided.")

        return data