'''
This file contains models for the app "users".
The following models will handle registration of users.
'''
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

# This is the custom user model which inherits from AbstractUser model.
# The reason behind this custom user model is to add additional fields which 
# django built-in User model doesn't have.
class CustomUser(AbstractUser):
    # These are the users roles for the school management system.
    # A user can either be a student, teacher or an admin.
    ROLE_CHOICES = (
        ('STUDENT', 'STUDENT'),
        ('TEACHER', 'TEACHER'),
        ('ADMIN', 'ADMIN')
    )

    # These are the gender choices.
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    # blank and null has been set True to allow the username to be set later since the system will
    # automatically give the user a username based on the user's role.
    username = models.CharField(unique=True, blank=True, null=True)
    other_names = models.CharField(max_length=100, blank=True, null=True) # it will store the middle names of users.
    role = models.CharField(max_length=20, choices=ROLE_CHOICES) # To identify to role of the user i.e Student, Teacher or Admin.
    profile_picture = models.ImageField(blank=True, null=True) # For identification purposes.
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) # Stores the gender of the user.
    date_of_birth = models.DateField(null=True, blank=True) # Stores the date of birth of the user.
    address = models.CharField(max_length=100) # Stores the address of the user.
    emergency_contact = models.CharField(max_length=15) # Stores the emergency contact of the user incase of emergencies.

    # This method handle the representation of all instances of the CustomUser model.
    # It displays the intances in the format "username last_name first_name other_names".
    # An example is 'STU-00011 Mpiani Ernest Kwasi'.
    def __str__(self):
        return f'{self.username} {self.last_name} {self.first_name} {self.other_names}'

    # The save method is being overriden to automatically generate username and password for a user when
    # being created.
    def save(self, *args, **kwargs):
        if not self.pk and not self.password: # This check for new users only.
            '''
            The code below checks if the user is a student.
            If the user is a student, it retrieves the last student created.
            If indeed a student was created before the current one, it takes the numeric part of 
            the student's ID(username), increase it by one and then sets it to be the numeric part of the
            new student being created. Otherwise, it sets the student's ID to be STU-00001, i.e.
            this is the first student being created.
            If the user is a teacher, the same process is done to set the username of the teacher being created.

            The password is automatically created using the last_name and username.
            The format is "last_name-username".
            An example is "Mpiani-STU00001"
            '''
            if self.role == 'STUDENT': # Checks if the user is a student
                last_student = CustomUser.objects.filter(role = 'STUDENT').last() # retrieves the last student created.
                if last_student: # checks if there is actually a student before the current one who is being created
                    last_student = str(last_student) # makes the last student a string which presents it in the '__str__' format defined above.
                    last_student_number = int(last_student[4:9]) # takes out the numeric part of the student's ID.
                    new_student_number = str(last_student_number + 1).zfill(5) # increase it by one, change is to a string and add zeros to the front to make it 5 characters to maintain consistency.
                    self.username = f'STU-{new_student_number}' # Now combine the student prefix(STU) with the new student numeric part to form the student ID which is the username.

                else: # if there is no last student, then this is the first student being created.
                    self.username = 'STU-00001' # The username is set to STU-00001 since this is the first student.

            elif self.role == 'TEACHER': # checks if the user is a teacher
                last_teacher = CustomUser.objects.filter(role = 'TEACHER').last() # retrieves the last teacher created.

                if last_teacher: # checks if there is actually a teacher before the current one who is being created.
                    last_teacher = str(last_teacher) # makes the last teacher a string which presents it in the '__str__' format defined above.
                    last_teacher_number = int(last_teacher[4:9]) # takes out the numeric part of the teacher's ID.
                    new_teacher_number = str(last_teacher_number + 1).zfill(5) # increase it by one, change it to a string and add zeros to the front to make it 5 characters to maintain consistency.
                    self.username = f'TEA-{new_teacher_number}' # Now combine the teacher prefix(TEA) with the new teacher numeric part to form the teacher ID which is the username.
                    
                else: # if there is no last teacher, then this is the last student being created.
                    self.username = 'TEA-00001' #The username is set to TEA-00001 since this is the first teacher.

            random_password = f'{self.last_name}-{self.username}'
            self._generated_password = random_password
            self.password = make_password(random_password)


        return super().save(*args, **kwargs)


# The student model is created to group all students in one place and also add additional information of students needed.
class Student(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile') # This links the student model to the customUser model.
    guardian_name = models.CharField(max_length=100) # This stores the name of the guardian of the student.
    guardian_address = models.CharField(max_length=100) # This stores the address of the guardian of the student.
    guardian_number = models.CharField(max_length=15) # This stores the phone number of the guardian of the student.

# The teacher model is created to group all teachers in one place and also add additional information of teachers needed.
class Teacher(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile') # This connects the teacher model to the CustomUser model
    # subject
    phone_number = models.CharField(max_length=15) # This saves the phone number of the teacher.