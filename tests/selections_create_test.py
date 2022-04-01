import pytest

@pytest.mark.django_db
def test_selection_create(client, selection, ads, user_token):
    data = {
        "name": selection.name,
        "owner": selection.owner.id,
        "items": [ads.id]}

    expected_response = {
        "id": 2,
        "name": "test_selection",
        "owner": 1,
        "items": [1]}

    response = client.post("/selection/create/",
                           data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + user_token)
    print(response.data)
    assert response.data == expected_response




