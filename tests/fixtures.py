import pytest
from ads.models import User

@pytest.fixture()
@pytest.mark.django_db
def user_token(client):
    username = "test75"
    password = "test75"

    response = client.post("/token/",
                           {"username": username,
                            "password": password},
                           content_type="application/json")
    return response.data['access']
