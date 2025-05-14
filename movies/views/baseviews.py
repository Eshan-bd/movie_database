from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     return Response({"detail": "GET not implemented."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def post(self, request, *args, **kwargs):
    #     return Response({"detail": "POST not implemented."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def put(self, request, *args, **kwargs):
    #     return Response({"detail": "PUT not implemented."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def delete(self, request, *args, **kwargs):
    #     return Response({"detail": "DELETE not implemented."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    pass

class BaseViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    pass
