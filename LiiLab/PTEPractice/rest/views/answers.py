from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import Answer
from ...utils import score_rmmcq_answer, score_ro_answer, score_sst_answer
from ..serializers.answers import AnswerSerializer

class AnswerCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.filter()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        answer = serializer.save(user=user)

        if answer.sst_question:
            score_sst_answer(answer)
        elif answer.ro_question:
            score_ro_answer(answer)
        elif answer.rmmcq_question:
            score_rmmcq_answer(answer)

class AnswerDetailView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = "pk"
