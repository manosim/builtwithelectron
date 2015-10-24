from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.directory.serializers import SubmitEntrySerializer


class SubmitEntryView(generics.CreateAPIView):

    serializer_class = SubmitEntrySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        tags = self.request.data['tags'].split(",") if self.request.data['tags'] else []
        serializer.save(author=self.request.user, tags=tags)
