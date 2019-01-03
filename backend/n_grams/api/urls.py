from django.urls import path

from .views import (
    WordListView,
    WordRetrieveView,
    WordCreateView,
    WordDestroyView,
    WordUpdateView,
    CharacterListView,
    CharacterCreateView,
    CharacterRetrieveView,
    CharacterDestroyView,
    CharacterUpdateView,
)

urlpatterns = [
    path('word/', WordListView.as_view()),
    path('word/create/', WordCreateView.as_view()),
    path('word/<pk>/', WordRetrieveView.as_view()),
    path('word/<pk>/delete/', WordDestroyView.as_view()),
    path('word/<pk>/update/', WordUpdateView.as_view()),
    path('character/', CharacterListView.as_view()),
    path('character/create/', CharacterCreateView.as_view()),
    path('character/<pk>/', CharacterRetrieveView.as_view()),
    path('character/<pk>/delete/', CharacterDestroyView.as_view()),
    path('character/<pk>/update/', CharacterUpdateView.as_view())
]
