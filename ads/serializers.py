from ads.models import Category, Location, User, Ads
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

"""    ADS create/update request 
{
    "name": "2test_test_test2",
    "category": "test",
    "author":{
        "username": "test100",
        "password": "test100",
        "birth_date": "2010-03-03",
        "email": "test100@yandex.ru"}
        }"""


def is_not_true(value):
    if value:
        raise serializers.ValidationError("This field can not be True")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AdsSerializer(ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Ads
        fields = "__all__"


class AdsListSerializer(ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Ads
        fields = ["id", "name", "category", "author"]


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

    is_published = serializers.BooleanField(validators=[is_not_true], required=False)

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop("author")
        self._category = self.initial_data.pop("category")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        try:
            author = User.objects.get(username=self._author['username'])
        except User.DoesNotExist:
            author = User.objects.create(username=self._author['username'],
                                         password=self._author['password'],
                                         birth_date=self._author['birth_date'],
                                         email=self._author['email'])

        category, _ = Category.objects.get_or_create(name=self._category)
        validated_data["author"] = author
        validated_data["category"] = category

        ads = Ads.objects.create(**validated_data)
        return ads

    class Meta:
        model = Ads
        fields = ["name", "category", "location", "is_published", "author"]


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
