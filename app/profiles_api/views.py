from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test APIView."""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Return a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete).',
            'Is similar to traditional Django View.',
            'Gives you the most control over your application logic.',
            'Is mapped manually to URLs.'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object."""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object."""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object."""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test APIviewset."""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello message."""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionally with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by id."""
        return Response({'http_method':'get'})

    def update(self, request, pk=None):
        """Handle updating an object."""
        return Response({'http_method':'put'})

    def partial_update(self, request, pk=None):
        """Handle partial_updating a object."""
        return Response({'http_method':'patch'})

    def destroy(self, request, pk=None):
        """Handle removing an object."""
        return Response({'http_method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
