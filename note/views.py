from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from note.models import Note
from note.serializers import NoteCreateSerializer, NoteSerializer


class NoteCreateView(CreateAPIView):
    model = Note
    serializer_class = NoteCreateSerializer
    permission_classes = [IsAuthenticated]


class NoteListView(ListAPIView):
    model = Note
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    ordering = ["-id"]
    queryset = Note.objects.all()

class NoteView(RetrieveUpdateDestroyAPIView):
    model = Note
    serializer_class = NoteSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()


    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Note
    fields = ["author", "text"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.logo = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "author": self.object.author,
            "text": self.object.text,
            "image": self.object.image.url,
        })