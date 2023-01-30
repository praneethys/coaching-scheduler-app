from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from app.models import Coach, Student, Schedule, Feedback

class CoachTestCase(TestCase):
    def setUp(self) -> None:
        Coach.objects.create(user_name="unit_test_coach_1", name="Unit Test Coach 1")

    def test_getCoachByUserName(self) -> None:
        getCoachByUserNameResponse = self.client.post(path='/getCoachByUserName/', data={'user_name': 'unit_test_coach_1'}, format='json', content_type='application/json')
        self.assertEqual(getCoachByUserNameResponse.status_code, 200)

class StudentTestCase(TestCase):
    def setUp(self) -> None:
        Student.objects.create(user_name="unit_test_student_1", name="Unit Test Student 1")

    def test_getStudentByUserName(self) -> None:
        getStudentByUserNameResponse = self.client.post(path='/getStudentByUserNameResponse/', data={'user_name': 'unit_test_student_1'}, format='json', content_type='application/json')
        self.assertEqual(getStudentByUserNameResponse.status_code, 200)


class ScheduleTestCase(TestCase):
    def setUp(self) -> None:
        Schedule.objects.create(coach_id=1,student_id=-1,begin_time=timezone.now(), end_time=timezone.now())
        Schedule.objects.create(coach_id=2,student_id=1,begin_time=timezone.now(), end_time=timezone.now())
        Schedule.objects.create(coach_id=3,student_id=-1,begin_time=timezone.now(), end_time=timezone.now())
    
    def test_getScheduleByCoach(self) -> None:
        getScheduleByCoachResponse = self.client.post(path='/getScheduleByCoach/', data={'coach_id': 3}, format='json', content_type='application/json')
        print(f'getScheduleByCoach: {getScheduleByCoachResponse}')
        self.assertEqual(getScheduleByCoachResponse.status_code, 200)

    def test_getScheduleByStudent(self) -> None:
        getScheduleByStudentResponse = self.client.post(path='/getScheduleByStudent/', data={'student_id': 1}, format='json', content_type='application/json')
        self.assertEqual(getScheduleByStudentResponse.status_code, 200)

    def test_setCoachAvailability(self) -> None:
        setCoachAvailabilityResponse = self.client.post(path='/setCoachAvailability/', data={'coach_id': 1, 'begin_time': timezone.now(), 'end_time': timezone.now()}, format='json', content_type='application/json')
        self.assertEqual(setCoachAvailabilityResponse.status_code, 200)

    def test_setAppointment(self) -> None:
        setAppointmentResponse = self.client.post(path='/setAppointment/', data={'schedule_id': 1, 'student_id': 2}, format='json', content_type='application/json')
        self.assertEqual(setAppointmentResponse.status_code, 200)

    def test_getAllAvailableAppointments(self) -> None:
        getAllAvailableAppointmentsResponse = self.client.get(path='/test_getAllAvailableAppointments/', content_type='application/json')
        print(f'getAllAvailableAppointmentsResponse: {getAllAvailableAppointmentsResponse}')
        self.assertEqual(getAllAvailableAppointmentsResponse.status_code, 200)

class FeedbackTestCase(TestCase):
    def setUp(self) -> None:
        Feedback.objects.create(schedule_id=1, rating=1, notes="unit test notes")
    
    def test_getFeedbackByScheduleId(self) -> None:
        getFeedbackByScheduleIdResponse = self.client.post(path='/getFeedbackByScheduleId/', data={'schedule_id': 1}, format='json', content_type='application/json')
        self.assertEqual(getFeedbackByScheduleIdResponse.status_code, 200)

    def test_submitFeedbackByScheduleId(self) -> None:
        submitFeedbackByScheduleIdResponse = self.client.post(path='/submitFeedbackByScheduleId/', data={'schedule_id': 2, 'rating': 4, 'notes': 'unit testing sample notes'}, format='json', content_type='application/json')
        self.assertEqual(submitFeedbackByScheduleIdResponse.status_code, 200)