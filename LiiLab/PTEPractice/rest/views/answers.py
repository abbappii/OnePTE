from rest_framework import generics
from ...models import Answer
from ..serializers.answers import AnswerSerializer
from ...tasks import score_answer_task

class AnswerCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.filter()

    def perform_create(self, serializer):
        user = self.request.user
        answer = serializer.save(user=user)
        score_answer_task.delay(answer.id)

class AnswerDetailView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = "pk"
