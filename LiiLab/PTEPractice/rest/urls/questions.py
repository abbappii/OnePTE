from django.urls import path
from ..views.questions import (
    QuestionListView,
    QuestionDetailView,
    SSTQuestionCreateView,
    ROQuestionCreateView,
    RMMCQQuestionCreateView,
)

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('sst/create/', SSTQuestionCreateView.as_view(), name='sst-question-create'),
    path('ro/create/', ROQuestionCreateView.as_view(), name='ro-question-create'),
    path('rmmcq/create/', RMMCQQuestionCreateView.as_view(), name='rmmcq-question-create'),
]