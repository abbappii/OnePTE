from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..serializers.questions import SSTQuestionSerializer, ROQuestionSerializer, RMMCQQuestionSerializer
from ...models import SSTQuestion, ROQuestion, RMMCQQuestion
from ...permissions import IsAdminUser

class SSTQuestionCreateView(generics.CreateAPIView):
    queryset = SSTQuestion.objects.all()
    serializer_class = SSTQuestionSerializer
    permission_classes = [IsAdminUser]

class ROQuestionCreateView(generics.CreateAPIView):
    queryset = ROQuestion.objects.all()
    serializer_class = ROQuestionSerializer
    permission_classes = [IsAdminUser]

class RMMCQQuestionCreateView(generics.CreateAPIView):
    queryset = RMMCQQuestion.objects.all()
    serializer_class = RMMCQQuestionSerializer
    permission_classes = [IsAdminUser]

'''
To Retrieve a list of question, i am using params 'type', for getting 3 of the question type in one API.
'''
class QuestionListView(generics.ListAPIView):

    def get_serializer_class(self):
        question_type = self.request.query_params.get('type', None)
        if question_type == 'SST':
            return SSTQuestionSerializer
        elif question_type == 'RO':
            return ROQuestionSerializer
        elif question_type == 'RMMCQ':
            return RMMCQQuestionSerializer

        return SSTQuestionSerializer

    def get_queryset(self):
        question_type = self.request.query_params.get('type', None)
        if question_type == 'SST':
            return SSTQuestion.objects.all()
        elif question_type == 'RO':
            return ROQuestion.objects.all()
        elif question_type == 'RMMCQ':
            return RMMCQQuestion.objects.all()

        return SSTQuestion.objects.none()

'''
To Retrieve a single question, i am using params 'type', for getting 3 of the question type in one API.
'''
class QuestionDetailView(generics.RetrieveUpdateAPIView):

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]

        return super().get_permissions()

    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        question_type = self.request.query_params.get('type', None)

        if question_type == 'SST':
            return SSTQuestion.objects.filter(id=question_id)
        elif question_type == 'RO':
            return ROQuestion.objects.filter(id=question_id)
        elif question_type == 'RMMCQ':
            return RMMCQQuestion.objects.filter(id=question_id)
        else:
            return SSTQuestion.objects.none()

    def get_serializer_class(self):
        question_type = self.request.query_params.get('type', None)

        if question_type == 'SST':
            return SSTQuestionSerializer
        elif question_type == 'RO':
            return ROQuestionSerializer
        elif question_type == 'RMMCQ':
            return RMMCQQuestionSerializer
        else:
            return SSTQuestionSerializer
