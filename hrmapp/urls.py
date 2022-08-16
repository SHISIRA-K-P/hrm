from django.contrib import admin
from django.urls import path

from hrmapp.views import LeaveView,LeaveDetailView,FeedbackView,FeedbackDetailView,StatusUpdateView

urlpatterns = [
path("leave",LeaveView.as_view()),
path("leave/<int:id>",LeaveDetailView.as_view()),
path("feedback",FeedbackView.as_view()),
path("feedback/<int:id>",FeedbackDetailView.as_view()),
path("status/<int:id>",StatusUpdateView.as_view())

]