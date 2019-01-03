from rest_framework import serializers

from n_grams.models import WordType, CharacterType, Document


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordType
        fields = ('token', 'vector', 'frequency')


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterType
        fields = ('token', 'vector', 'frequency')


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'document')
