from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from project.directory.serializers import SubmitEntrySerializer


class SubmitEntryView(generics.CreateAPIView):

    serializer_class = SubmitEntrySerializer
    permission_classes = (IsAuthenticated,)
