# coaching-scheduler-app
A full-stack mini project website to help manage coaching scheduling.

### This app features the following:
#### NOTE: This v1.0 only has basic features that have been implemented within the 3 hour timeframe alloted for this mini project.

1. Coaches can add slots of availability to their calendars. These slots are always 2 hours long and each slot can be booked by exactly 1 student. For example, a coach might set these times as available: 2022-02-23 10am-12pm, 2022-02-23 12pm-2pm, 2022-03-02 5pm - 7pm.

2. Coaches can view their own upcoming schedule.

3. Students can view upcoming available times across all coaches’ calls.

4. Students can book a slot for a call (the full 2 hours).

5. Coaches should be able to review their past scores and notes for all of their calls.

6. After they complete a call with a student, coaches will record the student’s satisfaction (an integer 1-5) and write some free-form notes.

### Tests:
v1.0 contains basic tests to test backend APIs and database models.

### Tech Stack:
Frontend - Vue.js

Backend  - Python with Django ORM

Database - SQLite

### Architecture:
The app architecture is very simple and straightforward. The app allows a person to login as a Coach or Student and view their respective dashboards.

![image](https://user-images.githubusercontent.com/61710414/215510598-3eff1eb1-a844-4401-8a38-249fa5d02f38.png)


<img width="1920" alt="er" src="https://user-images.githubusercontent.com/61710414/215511224-895a5da6-7f1a-43f1-b8b4-440311819987.png">

### Future:
#### UI
1. Display Coach name, Student name in the dashboards
2. Ability for Coach to cancel or change their availability
3. Ability for Coach to set availability in any timezone
4. Ability for Student to cancel an already scheduled future appointment
5. Ability for Coach to edit an already submitted feedback
6. Ability for Coach to share feedback with a Student
#### Infra / UI
1. Website login authentication
2. Frontend <-> Backend API authentication
3. Backend <-> Database connection authentication 
4. Offline mode
5. App accessibility considerations
6. Ability to switch between Light/dark modes
7. Ability to integrate with GCal
8. Make the website more mobile friendly
#### Backend
1. Validation for Coach availability dates. i.e., dates are not in the past, a selected availability shouldn't overlap an already existing slot for a given Coach, begin and end times of a slot are always 2 hours apart etc.
#### Tests
1. Frontend unit tests
2. Enhance backend unit tests
3. End-to-end tests

