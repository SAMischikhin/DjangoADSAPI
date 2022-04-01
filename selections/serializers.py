from ads.models import Selection
from ads.serializers import AdsSerializer
from rest_framework.serializers import ModelSerializer

#Response for selection create
"""{
    "name": "test_selection",
    "owner": 36,
    "items": [21, 26]}"""


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(ModelSerializer):
    items = AdsSerializer(many=True, read_only=True)

    class Meta:
        model = Selection
        fields = "__all__"
