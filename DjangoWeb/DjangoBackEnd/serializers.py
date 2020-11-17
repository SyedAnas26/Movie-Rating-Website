from rest_framework import serializers
from DjangoBackEnd.models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('MovieId',
                  'MovieTitle',
                  'ReleaseDate',
                  'MovieImage')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('MovieId',
                  'UpVotes',
                  'DownVotes',
                  'Rating')
