import pytest


@pytest.mark.django_db
def test_adlist_get(client, ads, user, category):
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": ads.id,
                "name": ads.name,
                "category": {
                    "id": category.id,
                    "name": category.name},
                "author": {
                    "username": user.username,
                    "password": user.password,
                    "location": None
                }}]}
    response = client.get("/ad/list/")
    print(response.data)

    assert response.data == expected_response


