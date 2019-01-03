from django.urls import path

from .views import (
    WordListView,
    WordRetrieveView,
    WordCreateView,
    WordDestroyView,
    WordUpdateView
)

urlpatterns = [
    path('', WordListView.as_view()),
    path('create/', WordCreateView.as_view()),
    path('<pk>/', WordRetrieveView.as_view()),
    path('<pk>/delete/', WordDestroyView.as_view()),
    path('<pk>/update/', WordUpdateView.as_view())
]
