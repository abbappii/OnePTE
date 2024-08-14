from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import generics

from ..serializers.questions import SSTQuestionSerializer, ROQuestionSerializer, RMMCQQuestionSerializer
from ...models import SSTQuestion, ROQuestion, RMMCQQuestion

class SSTQuestionCreateView(generics.CreateAPIView):
    queryset = SSTQuestion.objects.all()
    serializer_class = SSTQuestionSerializer

class ROQuestionCreateView(generics.CreateAPIView):
    queryset = ROQuestion.objects.all()
    serializer_class = ROQuestionSerializer

class RMMCQQuestionCreateView(generics.CreateAPIView):
    queryset = RMMCQQuestion.objects.all()
    serializer_class = RMMCQQuestionSerializer

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
class QuestionDetailView(generics.RetrieveAPIView):
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
