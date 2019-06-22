from django.urls import path

from .views import CategoryView, SingleCategoryView, ItemView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:pk>', SingleCategoryView.as_view()),

    path('items/', ItemView.as_view()),
]
