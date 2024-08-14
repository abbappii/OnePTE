from django.urls import path
from ..views.answers import (
    AnswerCreateView,
    AnswerDetailView,
)

urlpatterns = [
    path('', AnswerCreateView.as_view(), name='answer-create'),
    path('<int:pk>/', AnswerDetailView.as_view(), name='answer-detail'),
]
