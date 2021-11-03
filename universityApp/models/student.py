from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .career import Career


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
            Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser, PermissionsMixin):

    id = models.IntegerField(primary_key=True, unique=True)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Name', max_length=45)
    lastname = models.CharField('Lastname', max_length=45)
    birthdate = models.DateField('Birthdate')
    gender = models.CharField("Gender", max_length=15)
    phone = models.CharField("Phone", max_length=15)
    email = models.EmailField('Email', max_length=100)
    career = models.ForeignKey(
        Career, on_delete=models.CASCADE)

    objects = UserManager()  # objeto de la clase usermanager, atributo de la clase user()
    USERNAME_FIELD = 'id'

    @property
    def is_staff(self):
        return self.is_superuser
