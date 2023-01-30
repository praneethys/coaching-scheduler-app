from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from app.models import Coach, Student, Feedback, Schedule
from app.serializers import CoachSerializer, StudentSerializer, FeedbackSerializer, ScheduleSerializer, SetAvailabilitySerializer, SetAppointmentSerializer

@csrf_exempt
@api_view(['POST'])
def getCoachByUserName(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)
    print(f'/getCoachByUserName received request_payload: {request_payload}')

    try:
        coach = Coach.objects.filter(user_name = request_payload['user_name'])
        print(f'coach: {repr(coach)}')
    except:
        error_message = 'Failed to fetch coach for ' + str(request_payload['user_name'])
        return JsonResponse(error_message, safe=False)

    
    coach_serializer = CoachSerializer(coach, many=True)
    print(f'coach_serializer: {repr(coach_serializer.data)}')

    return JsonResponse(coach_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def getStudentByUserName(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)
    print(f'/getStudentByUserName received request_payload: {request_payload}')

    try:
        student = Student.objects.filter(user_name = request_payload['user_name'])
        print(f'student: {repr(student)}')
    except:
        error_message = 'Failed to fetch student for ' + str(request_payload['user_name'])
        return JsonResponse(error_message, safe=False)

    
    student_serializer = StudentSerializer(student, many=True)
    print(f'student_serializer: {repr(student_serializer.data)}')

    return JsonResponse(student_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def getScheduleByCoach(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    try:
        schedule = Schedule.objects.filter(coach_id = request_payload['coach_id'])
        print(f'schedule: {schedule.query}')
    except:
        error_message = 'Failed to fetch schedule for ' + str(request_payload['coach_id'])
        return JsonResponse(error_message, safe=False)

    schedule_serializer = ScheduleSerializer(schedule, many=True)
    print(f'schedule_serializer: {repr(schedule_serializer.data)}')
    
    return JsonResponse(schedule_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def getScheduleByStudent(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    try:
        schedule = Schedule.objects.filter(student_id = request_payload['student_id'])
        print(f'schedule: ${repr(schedule)}')
    except:
        error_message = 'Failed to fetch schedule for ' + str(request_payload['student_id'])
        return JsonResponse(error_message, safe=False)

    schedule_serializer = ScheduleSerializer(schedule, many=True)
    print(f'schedule_serializer: {repr(schedule_serializer.data)}')
    
    return JsonResponse(schedule_serializer.data, safe=False)


@csrf_exempt
@api_view(['POST'])
def setCoachAvailability(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    try:
        coach = Coach.objects.get(id = request_payload['coach_id'])
        print(f'coach: ${repr(coach)}')
    except:
        error_message = 'Failed to fetch coach for ' + str(request_payload['coach_id'])
        return JsonResponse(error_message, safe=False)

    schedule_serializer = SetAvailabilitySerializer(data=request_payload)
    if schedule_serializer.is_valid(raise_exception=True):
        schedule_serializer.save()
        print(f'schedule_serializer: {repr(schedule_serializer.data)}')

    return JsonResponse(schedule_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def setAppointment(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    try:
        schedule = Schedule.objects.get(id = request_payload['schedule_id'])
        print(f'schedule: ${repr(schedule)}')
    except:
        error_message = 'Failed to fetch schedule for ' + str(request_payload['schedule_id'])
        return JsonResponse(error_message, safe=False)

    schedule_serializer = SetAppointmentSerializer(data=request_payload)
    if schedule_serializer.is_valid(raise_exception=True):
        schedule_serializer.update(schedule, validated_data=schedule_serializer.validated_data)
        print(f'schedule_serializer: {repr(schedule_serializer.data)}')

    return JsonResponse(schedule_serializer.data, safe=False)

@csrf_exempt
@api_view(['GET'])
def getAllAvailableAppointments(request) -> JsonResponse:
    try:
        schedule = Schedule.objects.filter(student_id = -1)
        print(f'schedule: ${repr(schedule)}')
    except:
        error_message = 'Failed to fetch all available schedules'
        return JsonResponse(error_message, safe=False)

    schedule_serializer = ScheduleSerializer(schedule, many=True)
    return JsonResponse(schedule_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def getFeedbackByScheduleId(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    try:
        feedback = Feedback.objects.filter(schedule_id = request_payload['schedule_id'])
        print(f'feedback: ${repr(feedback)}')
    except:
        error_message = 'Failed to fetch feedback for ' + str(request_payload['schedule_id'])
        print(error_message)
        return JsonResponse([], safe=False)

    feedback_serializer = FeedbackSerializer(feedback, many=True)
    return JsonResponse(feedback_serializer.data, safe=False)

@csrf_exempt
@api_view(['POST'])
def submitFeedbackByScheduleId(request) -> JsonResponse:
    request_payload = JSONParser().parse(request)

    feedback_serializer = FeedbackSerializer(data=request_payload)
    if feedback_serializer.is_valid(raise_exception=True):
        feedback_serializer.save()
        print(f'feedback_serializer: {repr(feedback_serializer.data)}')

    return JsonResponse(feedback_serializer.data, safe=False)