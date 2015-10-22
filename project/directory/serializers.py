from rest_framework import serializers
from project.directory.models import Entry


class SubmitEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('name', 'short_description', 'website_url', 'user', 'tags')
