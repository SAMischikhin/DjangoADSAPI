from django.urls import path

from ads import views



urlpatterns = [
    path('list/',  views.AdsListView.as_view()),
    path('', views.AdsCreateView.as_view()),
    path('<int:pk>/', views.AdsDetailView.as_view()),
    path('<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('<int:pk>/delete/', views.AdsDeleteView.as_view()),
    path('<int:pk>/upload_image/', views.UploadImageView.as_view()),


    ]