from ads.models import Location, User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

""" Request for user create/update
{
    "username": "test75",
    "password": "test75",
    "birth_date" : "2000-03-03",
    "email": "test75@yandex.ru"
}"""

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserSerializer(ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = User
        fields = ["username", "password", "location"]


class UserCreateSerializer(ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name")

    def is_valid(self, raise_exception=False):
        if "location" in self.initial_data:
            self._location = self.initial_data.pop("location")
        else: self._location = None
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        if self._location != None:
            obj, _ = Location.objects.get_or_create(name=self._location)
            validated_data['location'] = obj

        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = ["username", "birth_date", "location"]


class UserUpdateSerializer(ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name")

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        obj, _ = Location.objects.get_or_create(name=self._location)
        self.validated_data['location'] = obj
        user = self.update(self.instance, self.validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"
