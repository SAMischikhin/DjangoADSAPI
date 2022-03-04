from django.urls import path

from cats import views


urlpatterns = [
    path('list/',  views.CategoryListView.as_view()),
    path('', views.CategoryCreateView.as_view()),
    path('<int:pk>/', views.CategoryDetailView.as_view()),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view()),

    ]