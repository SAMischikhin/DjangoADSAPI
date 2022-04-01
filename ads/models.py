import warnings
from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, EmailValidator
from django.db import models
from django.utils.deprecation import RemovedInDjango41Warning
from django.utils.encoding import punycode


def under_nine(value):
    if value > date.today() - timedelta(days=365*9):
        raise ValidationError("User under 9 can not be register")


class CustomEmailValidator(EmailValidator):

    def __init__(self, message=None, code=None, allowlist=None, *, whitelist=None, blacklist=None):
        self.domain_blacklist = blacklist
        super().__init__(message=None, code=None, allowlist=None, whitelist=None)

    def __call__(self, value):
        super().__call__(value)
        user_part, domain_part = value.rsplit('@', 1)
        if domain_part in self.domain_blacklist:
            raise ValidationError("rambler.ru domain dont access for registration", code=self.code, params={'value': value})



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=10, unique=True,
                            validators=[MinLengthValidator(5, 'the field must contain at least 5 characters')])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    lng = models.DecimalField(max_digits=8, decimal_places=6, default=0)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    MODERATOR = "moderator"
    MEMBER = "member"
    ROLES = [(MODERATOR, MODERATOR), (MEMBER, MEMBER)]
    role = models.CharField(max_length=30, choices=ROLES, default=MEMBER)
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True)
    birth_date = models.DateField(validators=[under_nine])
    email = models.EmailField(unique=True, validators=[CustomEmailValidator(blacklist=['rambler.ru'])])

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False,
                            validators=[MinLengthValidator(10, 'the field must contain at least 10 characters')])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, null=True, blank=True)

    
class Selection(models.Model):
    items = models.ManyToManyField(Ads)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

