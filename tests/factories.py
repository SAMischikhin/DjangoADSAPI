import factory
from ads.models import Ads, User, Category, Selection
from factory.django import DjangoModelFactory


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = "test75"
    password = "test75"
    birth_date = "2000-03-03"
    email = "test75@yandex.ru"


class AdsFactory(DjangoModelFactory):
    class Meta:
        model = Ads

    name = "test_test_test"
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)


class SelectionFactory(DjangoModelFactory):
    class Meta:
        model = Selection

    name = "test_selection"
    owner = factory.SubFactory(UserFactory)

    # @factory.post_generation
    # def groups(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #
    #     if extracted:
    #         for item in extracted:
    #             self.items.add(item)
