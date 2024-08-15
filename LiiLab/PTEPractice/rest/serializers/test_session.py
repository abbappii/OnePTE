from rest_framework import serializers
from ...models import TestSession

class TestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSession
        fields = ['id', 'user', 'sst_questions', 'ro_questions', 'rmmcq_questions', 'started_at', 'completed_at']
        read_only_fields = ["user"]
