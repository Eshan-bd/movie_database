from django.shortcuts import get_object_or_404
from imdb import IMDb
from rest_framework import status
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.views.baseviews import BaseAPIView


class MovieListView(BaseAPIView):
    serializer_class = MovieSerializer

    def get(self, request):
        queryset = Movie.objects.all()
        if queryset.exists():
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "No movies found."}, status=status.HTTP_404_NOT_FOUND)


class MovieDetailsView(BaseAPIView):

    def get(self, request, pk: int):
        # Initialize IMDb instance
        ia = IMDb()

        try:
            # Fetch the movie by its ID
            movie = get_object_or_404(Movie, id=pk)
            movie = ia.get_movie(movie.imdb_id)

            # Get movie details
            movie_details = {
                "description": movie.get('plot', ['N/A'])[0],  # Get plot description
                "releaseDate": movie.get('year', 'N/A'),
                "director": [director['name'] for director in movie.get('directors', [])],
                "cast": [actor['name'] for actor in movie.get('cast', [])],
                "runtime": movie.get('runtime', ['N/A'])[0],  # In minutes
                "rating": movie.get('rating', 'N/A'),
                "trailerUrl": None,  # IMDbPY does not provide trailer URL directly
                "reviews": []  # IMDbPY does not provide review excerpts directly
            }

            return Response(movie_details, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
