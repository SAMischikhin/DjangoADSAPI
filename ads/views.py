from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from ads.models import Category, Ads, User
from django_HT28.settings import TOTAL_ON_PAGE
import json


class Index(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


class AdListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("-price")
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        items = []
        for item in page_obj:
            items.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "author_id": item.author.id,
                    "price": item.price,
                    "description": item.description,
                    "is_published": item.is_published,
                    "category_id": item.category.id,
                    "image": item.image.url if item.image else ""
                }
            )

        response = {
            "items": items,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False, status=200)


class AdDetailView(DetailView):
    model = Ads

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.object.name,
                "author_id": self.object.author.id,
                "price": self.object.price,
                "description": self.object.description,
                "is_published": self.object.is_published,
                "category_id": self.object.category.id,
                "image": self.object.image.url if self.object.image else ""
            })


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ads
    fields = ["name", "author_id", "price", "description", "is_published", "category_id", "image"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)

        item = Ads()
        item.name = ads_data["name"]
        item.price = ads_data["price"]
        item.description = ads_data["description"]

        item.author = get_object_or_404(User, pk=ads_data["author_id"])
        item.category = get_object_or_404(Category, pk=ads_data["category_id"])

        item.save()
        return JsonResponse(
            {
                "id": item.id,
                "name": item.name,
                "author_id": item.author.id,
                "price": item.price,
                "description": item.description,
                "is_published": item.is_published,
                "category_id": item.category.id,
                "image": item.image.url if item.image else ""
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ads
    fields = ["name", "author", "price", "description", "category", "image"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        self.name = ads_data["name"]
        self.price = ads_data["price"]
        self.description = ads_data["description"]

        self.author = ads_data["author_id"]
        self.category = ads_data["category_id"]


        self.object.save()

        return JsonResponse(
            {
                "name": self.name,
                "author_id": self.author,
                "price": self.price,
                "description": self.description,
                "category_id": self.category,
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
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

