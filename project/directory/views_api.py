from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.directory.serializers import SubmitEntrySerializer


class SubmitEntryView(generics.CreateAPIView):

    serializer_class = SubmitEntrySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        print("=======")
        print(request.data['name'])
        print(dir(request))
        print(request.data['cover'])
        print("=======")
        return self.create(request, *args, **kwargs)
