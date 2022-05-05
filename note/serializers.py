from rest_framework import serializers


class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ("id", "created", "updated", "user", "is_deleted")
        fields = "__all__"