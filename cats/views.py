from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from ads.models import Category
import json

from django_HT28.settings import TOTAL_ON_PAGE


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("name")
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        res = []
        for category in page_obj:
            res.append({
                "id": category.id,
                "name": category.name
            })
        response = {
            "items": res,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        return JsonResponse(
            {
                'id': self.object.id,
                'name': self.object.name
            })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category, _ = Category.objects.get_or_create(name=category_data["name"])

        category.save()
        return JsonResponse(
            {
                "id": category.id,
                "name": category.name
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        request_data = json.loads(request.body)
        self.name = request_data["name"]

        self.object.save()

        return JsonResponse(
            {
                "id": self.object.id,
                "name": self.name
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)
