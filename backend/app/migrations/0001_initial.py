# Generated by Django 4.1.5 on 2023-01-30 05:00

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('user_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schedule_id', models.IntegerField(default=-1)),
                ('rating', models.IntegerField(validators=[app.models.validateStudentRating])),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coach_id', models.IntegerField(default=-1)),
                ('student_id', models.IntegerField(default=-1)),
                ('begin_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['begin_time', 'end_time'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('user_name', models.CharField(max_length=256)),
            ],
        ),
    ]
