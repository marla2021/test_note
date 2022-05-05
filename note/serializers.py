from rest_framework import serializers

from note.models import Note


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ("id", "created", "updated", "user", "is_deleted")
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
