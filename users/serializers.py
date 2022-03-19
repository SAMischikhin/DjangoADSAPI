from ads.models import Location, User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

""" Request for user create/update
{
    "first_name": "test",
    "last_name": "test",
    "username": "updatedtestusername",
    "password": "test",
    "role": "farmer",
    "age": 100,
    "location": "Kirsanov, Plechanovskaya ul., 13"
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
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        print(validated_data)
        obj, _ = Location.objects.get_or_create(name=self._location)
        validated_data['location'] = obj

        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"


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
