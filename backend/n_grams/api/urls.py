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
    AllUploads,
    UploadText,
    ReadUpload
)
from n_grams.api import views

urlpatterns = [
    path('', AllUploads.as_view()),
    path('fileupload/', UploadText.as_view()),
    path('fileupload/<pk>', ReadUpload.as_view()),
    path('word/', WordListView.as_view()),
    path('words/', WordCreateView.as_view()),
    path('word/<pk>/', WordRetrieveView.as_view()),
    path('word/<pk>/delete/', WordDestroyView.as_view()),
    path('word/<pk>/update/', WordUpdateView.as_view()),
    path('character/', CharacterListView.as_view()),
    path('character/create/', CharacterCreateView.as_view()),
    path('character/<pk>/', CharacterRetrieveView.as_view()),
    path('character/<pk>/delete/', CharacterDestroyView.as_view()),
    path('character/<pk>/update/', CharacterUpdateView.as_view()),
]
