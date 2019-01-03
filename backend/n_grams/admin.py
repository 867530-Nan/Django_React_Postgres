from django.contrib import admin

# Register your models here.

from .models import CharacterType, WordType, Document

admin.site.register(CharacterType)
admin.site.register(WordType)
admin.site.register(Document)
