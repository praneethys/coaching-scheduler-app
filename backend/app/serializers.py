from rest_framework import serializers
from app.models import Coach, Student, Feedback, Schedule

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'name', 'user_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'user_name']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class SetAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['coach_id', 'begin_time', 'end_time']

class SetAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'student_id']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'