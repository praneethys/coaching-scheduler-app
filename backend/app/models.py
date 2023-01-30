from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validateStudentRating(value) -> None | ValidationError:
        if not 1 <= value <= 5:
            raise ValidationError(
                _('Invalid rating. Allowed values for rating are between 1-5. Given rating: %(value)'),
                params={'value': value},
            )

class Coach(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    user_name = models.CharField(max_length=256)

    def __str__(self) -> str:
         return self.user_name
    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    user_name = models.CharField(max_length=256)

    def __str__(self) -> str:
         return self.user_name

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    coach_id = models.IntegerField(default=-1)
    student_id = models.IntegerField(default=-1)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['begin_time', 'end_time']

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    schedule_id = models.IntegerField(default=-1)
    rating = models.IntegerField(validators=[validateStudentRating])
    notes = models.TextField()