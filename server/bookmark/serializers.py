from rest_framework import serializers
from base.models import Bookmark
from base.models import Tag
from base.models import Workspace

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tag
        fields = ['id', 'name']

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Workspace
        fields = ['id', 'name']

class BookmarkSerializer(serializers.ModelSerializer):
    tags       = TagSerializer(many=True, read_only=True)
    tag_ids    = serializers.PrimaryKeyRelatedField(
                     many=True,
                     queryset=Tag.objects.all(),
                     write_only=True,
                     source='tags'
                 )

    workspaces = WorkspaceSerializer(many=True, read_only=True)
    ws_ids     = serializers.PrimaryKeyRelatedField(
                     many=True,
                     queryset=Workspace.objects.all(),
                     write_only=True,
                     source='workspaces'
                 )

    class Meta:
        model = Bookmark
        fields = [
            'id', 'user', 'name', 'link', 'description',
            'status', 'created',
            'tags', 'workspaces',
            'tag_ids', 'ws_ids',
        ]
        read_only_fields = ['id', 'created']

    def create(self, validated_data):
        tags       = validated_data.pop('tags', [])
        workspaces = validated_data.pop('workspaces', [])
        bookmark = Bookmark.objects.create(**validated_data)
        bookmark.tags.set(tags)
        bookmark.workspaces.set(workspaces)
        return bookmark

    def update(self, instance, validated_data):
        tags       = validated_data.pop('tags', None)
        workspaces = validated_data.pop('workspaces', None)

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()

        if tags is not None:
            instance.tags.set(tags)
        if workspaces is not None:
            instance.workspaces.set(workspaces)
        return instance