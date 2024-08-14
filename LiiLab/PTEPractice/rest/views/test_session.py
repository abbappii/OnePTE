from rest_framework import generics
from ...models import TestSession
from ..serializers.test_session import TestSessionSerializer
from rest_framework.permissions import IsAuthenticated

class TestSessionCreateView(generics.ListCreateAPIView):
    queryset = TestSession.objects.all()
    serializer_class = TestSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        session = serializer.save(user=self.request.user)

class UserTestSessionListView(generics.ListAPIView):
    serializer_class = TestSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        question_type = self.request.query_params.get("type", None)
        sessions = TestSession.objects.filter(user=user).order_by('-started_at')

        if question_type:
            if question_type == 'SST':
                sessions = sessions.filter(sst_questions__isnull=False)
            elif question_type == 'RO':
                sessions = sessions.filter(ro_questions__isnull=False)
            elif question_type == 'RMMCQ':
                sessions = sessions.filter(rmmcq_questions__isnull=False)

        return sessions
