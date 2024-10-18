from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from bot.serializers import GroupSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import git




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
@api_view(['GET', 'POST'])
def update_server(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response({'100':100}, status=status.HTTP_100_CONTINUE)

    elif request.method == 'POST':
        repo = git.Repo('mysite')
        origin = repo.remotes.origin
        origin.pull()
        return Response({"result server update": "very nice"}, status=status.HTTP_200_OK )