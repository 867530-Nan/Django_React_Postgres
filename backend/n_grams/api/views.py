from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from n_grams.models import (
    WordType,
    CharacterType
)
from n_grams.api.serializers import (
    WordSerializer,
    CharacterSerializer
)


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
