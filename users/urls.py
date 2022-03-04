from django.urls import path
from users import views

urlpatterns = [
    path('list/',  views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('', views.UserCreateView.as_view()),
    path('<int:pk>/update/', views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
    ]