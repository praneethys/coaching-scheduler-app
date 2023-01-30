from django.urls import re_path
from app import views

urlpatterns = [
    re_path('getCoachByUserName', views.getCoachByUserName),
    re_path('getStudentByUserName', views.getStudentByUserName),
    re_path('getScheduleByCoach', views.getScheduleByCoach),
    re_path('getScheduleByStudent', views.getScheduleByStudent),
    re_path('setCoachAvailability', views.setCoachAvailability),
    re_path('setAppointment', views.setAppointment),
    re_path('getAllAvailableAppointments', views.getAllAvailableAppointments),
    re_path('getFeedbackByScheduleId', views.getFeedbackByScheduleId),
    re_path('submitFeedbackByScheduleId', views.submitFeedbackByScheduleId),
]
