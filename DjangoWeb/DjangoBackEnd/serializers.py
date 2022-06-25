from rest_framework import serializers
from DjangoBackEnd.models import MovieRating


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = ('MovieId',
                  'MovieTitle',
                  'ReleaseDate',
                  'MovieImage',
                  'UpVotes',
                  'DownVotes',
                  'Rating')
