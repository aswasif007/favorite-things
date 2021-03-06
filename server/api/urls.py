from django.urls import path

from .views import CategoryView, SingleCategoryView, ItemView, SingleItemView, SingleItemRankView, AuditLogView


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:pk>', SingleCategoryView.as_view()),

    path('items/', ItemView.as_view()),
    path('items/<str:pk>', SingleItemView.as_view()),
    path('items/<str:pk>/rank', SingleItemRankView.as_view()),

    path('audit_logs/', AuditLogView.as_view()),
]
