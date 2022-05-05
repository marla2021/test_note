
class CommentCreateView(CreateAPIView):
    model = GoalComment
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]