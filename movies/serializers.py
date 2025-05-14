from rest_framework import serializers

from movies.models import Genre, Movie


class BaseSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        # Add global validation logic here if needed
        return super().validate(attrs)

class GenreSerializer(BaseSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(BaseSerializer):
    genre = serializers.CharField(source='genre.name')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'poster']