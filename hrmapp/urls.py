from django.contrib import admin
from django.urls import path
from hrmapp.views import LeaveView, LeaveDetailView
from hrmapp.views import FeedbackView, FeedbackDetailView, StatusUpdateView

urlpatterns = [
    path("leave", LeaveView.as_view()),
    path("leave/<int:leave_id>", LeaveDetailView.as_view()),
    path("feedback", FeedbackView.as_view()),
    path("feedback/<int:feed_id>", FeedbackDetailView.as_view()),
    path("status/<int:status_id>", StatusUpdateView.as_view())
]
