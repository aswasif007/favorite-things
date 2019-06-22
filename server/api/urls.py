from django.urls import path

from .views import CategoryView, SingleCategoryView, ItemView, SingleItemView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:pk>', SingleCategoryView.as_view()),

    path('items/', ItemView.as_view()),
    path('items/<str:pk>', SingleItemView.as_view()),
]
