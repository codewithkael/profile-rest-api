from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self,request,format=None):
        """returns a list of apiviews"""
        an_apiview = [
        'Uses HTTPS methos as functions (get, post, patch, put, delete)',
        'Is similar to traditional Django View',
        'Gives you the most control over your application',
        ]

        return Response({'message': 'hello!','an_apiview': an_apiview})
