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


# class RatingSerializer(serializers.ModelSerializer):
#     Movie = MovieSerializer(read_only=True)
#
#     class Meta:
#         model = Rating
#         fields = ('Movie',
#                   'UpVotes',
#                   'DownVotes',
#                   'Rating')
