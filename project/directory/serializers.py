from rest_framework import serializers
from project.directory.models import Entry


class SubmitEntrySerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = ('name', 'short_description', 'website_url', 'repo_url', 'tags', 'cover', 'description')
