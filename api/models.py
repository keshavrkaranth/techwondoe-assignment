from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth.models import PermissionsMixin
import uuid


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, name, username, email, password=None):
        if not email:
            raise ValidationError('User must have email address')
        if not username:
            raise ValidationError('User must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name
        )
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, name, username, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save()
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    company_ceo = models.CharField(max_length=30)
    company_address = models.TextField()
    inception_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'company'


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    team_lead = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_lead

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'
