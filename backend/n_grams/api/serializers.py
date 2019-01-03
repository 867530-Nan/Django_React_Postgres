from rest_framework import serializers

from n_grams.models import WordType, CharacterType


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordType
        fields = ('token', 'vector', 'frequency')


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterType
        fields = ('token', 'vector', 'frequency')
