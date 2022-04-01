import pytest

@pytest.mark.django_db
def test_ad_create(client, ads, user):
    data ={
    "name": ads.name,
    "category": ads.category.name,
    "author":{
        "username": user.username,
        "password": user.password,
        "birth_date": user.birth_date,
        "email": user.email}
        }

    expected_response = {
        "name": "test_test_test",
        "category": "test_category",
        "is_published": False,
        "author": {
            "username": "test75",
            "birth_date": "2000-03-03",
            "location": None
            }
        }

    response = client.post("/ad/create/", data, content_type="application/json")

    assert response.data == expected_response



