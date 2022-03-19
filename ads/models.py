from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits= 8, decimal_places=6, default=0)
    lng = models.DecimalField(max_digits= 8, decimal_places=6, default=0)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    MODERATOR = "moderator"
    MEMBER = "member"
    ROLES = [(MODERATOR, MODERATOR), (MEMBER, MEMBER)]
    role = models.CharField(max_length=30, choices=ROLES, default=MEMBER)
    # role = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    
class Selection(models.Model):
    items = models.ManyToManyField(Ads)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

