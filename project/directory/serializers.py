from rest_framework import serializers
from rest_framework.fields import UUIDField
from project.directory.models import Entry


class SubmitEntrySerializer(serializers.ModelSerializer):
    # tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='tags', UUIDField(format='hex_verbose'))
    # tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True, pk_field=UUIDField(format='hex_verbose'))

    class Meta:
        model = Entry
        fields = ('name', 'short_description', 'website_url', 'repo_url', 'tags', 'cover', 'description')
