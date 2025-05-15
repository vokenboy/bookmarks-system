from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Bookmark
from rest_framework import status
from .serializers import BookmarkSerializer

@api_view(['GET'])
def get_bookmarks(request, user_id):
    qs = Bookmark.objects.filter(user_id=user_id)
    serializer = BookmarkSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bookmark(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return Response({'error': 'Bookmark not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BookmarkSerializer(bookmark)
    return Response(serializer.data)

@api_view(['POST'])
def post_bookmark(request):
    serializer = BookmarkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_bookmark(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return Response({'error': 'Bookmark not found'}, status=status.HTTP_404_NOT_FOUND)
    bookmark.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_bookmark(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        return Response({'error': 'Bookmark not found'},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = BookmarkSerializer(bookmark, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)