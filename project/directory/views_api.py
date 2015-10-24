from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.directory.serializers import SubmitEntrySerializer


class SubmitEntryView(generics.CreateAPIView):

    serializer_class = SubmitEntrySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        tags = []
        if self.request.data['tags']:
            tags = self.request.data['tags'].split(",")
        serializer.save(author=self.request.user, tags=tags)
