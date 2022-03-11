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


class User(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30) #только en
    password = models.CharField(max_length=30) #специальное поле?
    role = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)#, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
