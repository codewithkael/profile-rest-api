from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import permissions

class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """returns a list of apiviews"""
        an_apiview = [
        'Uses HTTPS methos as functions (get, post, patch, put, delete)',
        'Is similar to traditional Django View',
        'Gives you the most control over your application',
        ]

        return Response({'message': 'hello!','an_apiview': an_apiview})

    def post(self,request):
        """ create a hello message with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        """handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self,request,pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method': "DELETE"})

class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""

        a_viewset = ['aaaa',
        'bbbb','cccc','dddd']

        return Response({'message': 'hello', 'a_viewset' : a_viewset})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve (self,request,pk=None):
        """handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update (self,request,pk=None):
        """handle updating an object"""
        return Response({'http_method': 'UPDATE'})

    def partial_update (self,request,pk=None):
        """handle updating  part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy (self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
    
