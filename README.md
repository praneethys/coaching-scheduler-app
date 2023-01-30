# coaching-scheduler-app
A full-stack mini project website to help manage coaching scheduling.

This app features the following:
1. Coaches can add slots of availability to their calendars. These slots are always 2 hours long and each slot can be booked by exactly 1 student. For example, a coach might set these times as available: 2022-02-23 10am-12pm, 2022-02-23 12pm-2pm, 2022-03-02 5pm - 7pm.

2. Coaches can view their own upcoming schedule.

3. Students can view upcoming available times across all coaches’ calls.

4. Students can book a slot for a call (the full 2 hours).

5. Coaches should be able to review their past scores and notes for all of their calls.

6. After they complete a call with a student, coaches will record the student’s satisfaction (an integer 1-5) and write some free-form notes.

Tools:
Frontend - Vue.js
Backend  - Python with Django ORM
Database - SQLite

The app architecture is very simple and straightforward. The app allows a person to login as a Coach or Student and view their respective dashboards.

![image](https://user-images.githubusercontent.com/61710414/215510598-3eff1eb1-a844-4401-8a38-249fa5d02f38.png)


![image](https://user-images.githubusercontent.com/61710414/215510973-84e36676-9718-47d2-adc9-7eaa67c04f18.png)

