from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name

class UserManager(DefaultUserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Get the role instance for the superuser
        role = Role.objects.get(role_name='Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        extra_fields['role'] = role  # Set the role as an attribute

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['email', 'role']

    objects = UserManager()

    def __str__(self):
        return self.username



# from django.db import models

# class Role(models.Model):
#     role_name = models.CharField(max_length=100)

# class Faculty(models.Model):
#     faculty_name = models.CharField(max_length=100)

# class Department(models.Model):
#     department_name = models.CharField(max_length=100)

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)