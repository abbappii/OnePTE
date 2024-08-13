from django.urls import path, include

urlpatterns = [
    path("questions/", include("PTEPractice.rest.urls.questions")),
    path("answers/", include("PTEPractice.rest.urls.answers")),
    path("test-sessions/", include("PTEPractice.rest.urls.test_session")),
]
