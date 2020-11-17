from django.shortcuts import render
from rest_framework.parsers import JSONParser

from DjangoBackEnd.models import Movie, Rating
from DjangoBackEnd.serializers import MovieSerializer, RatingSerializer
from django.http.response import JsonResponse


# Create your views here.

def getMovies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    else:
        return JsonResponse(" This method allows only GET method ")


def getRatings(request):
    if request.method == 'GET':
        ratings = Rating.objects.all()
        rating_serializer = RatingSerializer(ratings, many=True)
        return JsonResponse(rating_serializer.data, safe=False)
    elif request.method == 'PUT':
        ratings_data = JSONParser().parse(request)
        rating_for = Rating.objects.get(MovieId=ratings_data['MovieId'])
        rating_serializer = RatingSerializer(rating_for, data=ratings_data)
        if rating_serializer.is_valid():
            rating_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    else:
        return JsonResponse(" This method allows only GET,PUT methods ")


