import time

from rest_framework.decorators import action

from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.views.baseviews import BaseViewSet


class MovieViewSet(BaseViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    # def list(self, request, *args, **kwargs):
    #     time.sleep(2)  # Adds a 2-second delay before responding
    #     return super().list(request, *args, **kwargs)