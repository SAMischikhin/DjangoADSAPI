from ads.serializers import AdsSerializer, AdsCreateSerializer,  AdsUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from users.serializers import LocationSerializer

from django.http import JsonResponse
from django.views.generic import UpdateView

from ads.models import Ads, Location

from rest_framework.generics import ListAPIView, RetrieveAPIView,\
    CreateAPIView, UpdateAPIView, DestroyAPIView


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()#.order_by("-price")
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        ads_description = request.GET.get("text", None)
        category_id = request.GET.get("cat_id", None)
        location = request.GET.get("location", None)
        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_from", None)


        if ads_description:
            self.queryset = self.queryset.filter(name__contains=ads_description)

        if category_id:
            self.queryset = self.queryset.filter(category_id=category_id)

        if location:
            self.queryset = self.queryset.filter(author__location__name__contains=location)

        if bool(price_from) and bool(price_to):
            self.queryset = self.queryset.filter(price__range=[price_from, price_to])

        return super().get(request, *args, **kwargs)

class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer


class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class UploadImageView(UpdateView):
    model = Ads
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "image": self.object.image.url
            }
        )


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
