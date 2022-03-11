from ads.models import Category, Location, User, Ads
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

"""    ADS create/update request 
    {
    "name": "test",
    "author": {
        "username": "Сережа",
        "password": "abc123",
        "location": "St-Peterburg"},
    "price": 100,
    "description": "test",
    "category": "ПС"
    }
    """


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdsSerializer(ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Ads
        fields = "__all__"


class AdsCreateSerializer(ModelSerializer):
    author = UserCreateSerializer(required=False)

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name")

    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name")

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data["author"].pop("location")
        self._author = self.initial_data.pop("author")
        self._category = self.initial_data.pop("category")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        location, _ = Location.objects.get_or_create(name=self._location)

        author, _ = User.objects.get_or_create(username=self._author['username'],
                                               password=self._author['password'],
                                               location=location)
        category, _ = Category.objects.get_or_create(name=self._category)
        validated_data["author"] = author
        validated_data["category"] = category

        ads = Ads.objects.create(**validated_data)
        return ads

    class Meta:
        model = Ads
        fields = "__all__"


class AdsUpdateSerializer(ModelSerializer):
    author = UserUpdateSerializer(required=False)

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field="name")

    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name")

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data["author"].pop("location")
        self._author = self.initial_data.pop("author")
        self._category = self.initial_data.pop("category")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        location, _ = Location.objects.get_or_create(name=self._location)

        author, _ = User.objects.get_or_create(username=self._author['username'],
                                               password=self._author['password'],
                                               location=location)
        category, _ = Category.objects.get_or_create(name=self._category)
        self.validated_data["author"] = author
        self.validated_data["category"] = category

        ads = self.update(self.instance, self.validated_data)
        ads.save()
        return ads

    class Meta:
        model = Ads
        fields = "__all__"
