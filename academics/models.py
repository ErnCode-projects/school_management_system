'''
This models.py contain the subject and class model.
Subject and Class_Level models are linked to Teachers and Student respectively in the users/models.py.
'''
from django.db import models

# This is the Subject model which handles subjects taught in the school.
class Subject(models.Model):
    subject_name = models.CharField(max_length=50) # This takes the name of the subject.

    def __str__(self):
        return f'{self.subject_name}'

# This is the Class_Level model which handles the various classes in the school.
class Class_Level(models.Model):
    # These are the choices for the division within classes.
    STREAM_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
    )

    class_name = models.CharField(max_length=50) # This takes the name of the class.
    class_stream = models.CharField(max_length=2, choices=STREAM_CHOICES) # This helps to separate the division within classes.
    class_teacher = models.OneToOneField('users.Teacher', on_delete=models.SET_NULL, null=True, related_name='class_level_teacher') # This connects a class to one teacher who handles the basic activities of a class.
    subject_teachers = models.ManyToManyField('users.Teacher', related_name='classes_taught') # This connects the class to the different teachers who teach different subjects in the class.
    academic_year = models.CharField(max_length=15) # This represents the school year a class belongs to.

    def __str__(self):
        return f'{self.class_name} {self.class_stream}'