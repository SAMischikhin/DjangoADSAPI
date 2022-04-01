from pytest_factoryboy import register
from tests.factories import UserFactory, AdsFactory, CategoryFactory, SelectionFactory

#Factory
register(UserFactory)
register(AdsFactory)
register(CategoryFactory)
register(SelectionFactory)

#Fixtures
pytest_plugins = "tests.fixtures"

