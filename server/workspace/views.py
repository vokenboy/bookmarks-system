from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Workspace
from .serializers import WorkspaceSerializer


@api_view(['GET'])
def get_workspaces(request, user_id):
    qs = Workspace.objects.filter(user_id=user_id)
    serializer = WorkspaceSerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_workspace(request, pk):
    try:
        workspace = Workspace.objects.get(id=pk)
        serializer = WorkspaceSerializer(workspace, many=False)
        return Response(serializer.data)
    except Workspace.DoesNotExist:
        return Response({'error': 'Workspace not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_workspace(request):
    serializer = WorkspaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def update_workspace(request, pk):
    try:
        workspace = Workspace.objects.get(id=pk)
        serializer = WorkspaceSerializer(workspace, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Workspace.DoesNotExist:
        return Response({'error': 'Workspace not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_workspace(request, pk):
    try:
        workspace = Workspace.objects.get(id=pk)
        workspace.delete()
        return Response({'message': 'Workspace deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Workspace.DoesNotExist:
        return Response({'error': 'Workspace not found'}, status=status.HTTP_404_NOT_FOUND)
