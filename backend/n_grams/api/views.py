from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from n_grams.models import WordType
from n_grams.api.serializers import WordSerializer


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
