from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from ads.models import Category, Ads, User, Location
from django_HT28.settings import TOTAL_ON_PAGE
import json


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("username")
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        items = []
        for item in page_obj:
            items.append({
                "id": item.id,
                "username": item.username,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "role": item.role,
                "age": item.age,
                "location": item.location.name,
                "total_ads": len([n for n in list(Ads.objects.values('author')) if n['author']==item.id])
            })

        response = {
            "items": items,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)

        return JsonResponse(
            {
                "id": self.object.id,
                "username": self.object.username,
                "first_name": self.object.first_name,
                "last_name": self.object.last_name,
                "role": self.object.role,
                "age": self.object.age,
                "location": self.object.location.name,
            })


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        item = User()
        item.username = user_data["username"]
        item.first_name = user_data["first_name"]
        item.last_name = user_data["last_name"]
        item.role = user_data["role"]
        item.age = user_data["age"]

        item.location = get_object_or_404(Location, pk=user_data["location_id"])

        item.save()
        return JsonResponse(
            {
                "id": item.id,
                "username": item.username,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "role": item.role,
                "age": item.age,
                "location_id": item.location.name if item.location else '',
            })


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.username = user_data["username"]
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.role = user_data["role"]
        self.object.age = user_data["age"]
        self.object.location = get_object_or_404(Location, pk=user_data["location_id"])

        self.object.save()
        return JsonResponse(
            {
                "id": self.object.id,
                "username": self.object.username,
                "first_name": self.object.first_name,
                "last_name": self.object.last_name,
                "role": self.object.role,
                "age": self.object.age,
                "location_id": self.object.location.name,
            })


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


