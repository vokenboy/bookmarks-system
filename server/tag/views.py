from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Tag
from rest_framework import status
from .serializers import TagSerializer


@api_view(['GET'])
def get_tags(request, user_id):
    tags = Tag.objects.filter(user_id=user_id).order_by('name')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_tag(request):
    name    = request.data.get('name')
    user_id = request.data.get('user')

    if not name or not user_id:
        return Response(
            {'error': 'Both "name" and "user" fields are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    tag, created = Tag.objects.get_or_create(
        user_id=user_id,
        name=name
    )
    if not created:
        return Response(
            {'error': f'Tag "{name}" already exists for this user.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def delete_tag(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(
            {'error': 'Tag not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
