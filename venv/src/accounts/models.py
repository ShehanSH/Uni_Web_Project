from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(DefaultUserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        role = Role.objects.get(role_name='Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        extra_fields['role'] = role

        return self._create_user(username, email, password, **extra_fields)




class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['email', 'role', 'date_of_birth', 'gender', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.username

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=255)

    def __str__(self):
        return self.faculty_name 

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name
    
class UniversityPerson(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(primary_key=True, max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['student_id', 'faculty', 'user', 'department']

class UniversityStaffPerson(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    staff_type = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['staff_id', 'faculty', 'user', 'department']
    

class Outsider(models.Model):
    nic = models.CharField(primary_key=True, max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['nic', 'user']

  



