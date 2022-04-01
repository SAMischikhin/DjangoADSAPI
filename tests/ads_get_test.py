import pytest


@pytest.mark.django_db
def test_ad_get(client, ads, user, category, user_token):
    expected_response = {
        "id": ads.id,
        "author": {
            "username": user.username,
            "password": user.password,
            "location": None},
        "category": {
            "id": category.id,
            "name": category.name},
        "name": ads.name,
        "price": None,
        "description": None,
        "image": None,
        "is_published": False}

    response = client.get("/ad/1/", HTTP_AUTHORIZATION="Bearer " + user_token)
    print(response.data)

    assert response.data == expected_response
