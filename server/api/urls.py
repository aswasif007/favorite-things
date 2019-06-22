from django.urls import path

from .views import CategoryView, SingleCategoryView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
]
