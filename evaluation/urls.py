from django.urls import path
from .views import ProductListView, EvaluationCreateView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('evaluations/', EvaluationCreateView.as_view()),
]