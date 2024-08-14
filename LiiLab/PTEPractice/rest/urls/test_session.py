from django.urls import path
from ..views.test_session import TestSessionCreateView, UserTestSessionListView

urlpatterns = [
    path('', TestSessionCreateView.as_view(), name='test-session-create'),
    path('me/', UserTestSessionListView.as_view(), name='user-test-session-list'),
]