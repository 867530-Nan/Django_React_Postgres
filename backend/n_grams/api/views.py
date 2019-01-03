from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from n_grams.models import (
    WordType,
    CharacterType,
    Document
)
from n_grams.api.serializers import (
    WordSerializer,
    CharacterSerializer,
    UploadSerializer
)

from django.shortcuts import render, redirect

from .forms import DocumentForm


class AllUploads(ListAPIView):
    print("get them all")
    queryset = Document.objects.all()
    serializer_class = UploadSerializer


class UploadText(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = UploadSerializer


class ReadUpload(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = UploadSerializer

# def model_form_upload(request):
#     print("asdfasdfasdfasd")
#     print(request.method)
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'forms/model_form_upload.html', {
#         'form': form
#     })


class WordListView(ListAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordSerializer


class WordCreateView(CreateAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordSerializer


class WordRetrieveView(RetrieveAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordSerializer


class WordDestroyView(DestroyAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordSerializer


class WordUpdateView(UpdateAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordSerializer


class CharacterListView(ListAPIView):
    queryset = CharacterType.objects.all()
    serializer_class = CharacterSerializer


class CharacterCreateView(CreateAPIView):
    queryset = CharacterType.objects.all()
    serializer_class = CharacterSerializer


class CharacterRetrieveView(RetrieveAPIView):
    queryset = CharacterType.objects.all()
    serializer_class = CharacterSerializer


class CharacterDestroyView(DestroyAPIView):
    queryset = CharacterType.objects.all()
    serializer_class = CharacterSerializer


class CharacterUpdateView(UpdateAPIView):
    queryset = CharacterType.objects.all()
    serializer_class = CharacterSerializer
