from django.shortcuts import render
from pipenv.vendor.tomlkit.items import Integer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from DjangoBackEnd.models import MovieRating
from DjangoBackEnd.serializers import MovieRatingSerializer
from django.http.response import JsonResponse


# Create your views here.
@csrf_exempt
def getMovies(request):
    if request.method == 'GET':
        movies = MovieRating.objects.all()
        movie_serializer = MovieRatingSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)
    else:
        return JsonResponse(" This method allows only GET method ")


@csrf_exempt
def RatingsApi(request):
    if request.method == 'PUT':
        if request.path == '/upvote/':
            ratings_data = JSONParser().parse(request)
            rating_for = MovieRating.objects.get(MovieId=ratings_data['MovieId'])
            rating_for.UpVotes = ratings_data['UpVotes']
            rating_for.Rating = (int(rating_for.UpVotes) / (int(rating_for.UpVotes) + (
                int(rating_for.DownVotes)))) * 10
            rating_for.save()
            return JsonResponse("Updated Successfully!!", safe=False)

        else:
            ratings_data = JSONParser().parse(request)
            rating_for = MovieRating.objects.get(MovieId=ratings_data['MovieId'])
            rating_for.DownVotes = ratings_data['DownVotes']
            rating_for.Rating = (int(rating_for.UpVotes) / (int(rating_for.UpVotes) + (
                int(rating_for.DownVotes)))) * 10
            rating_for.save()
            return JsonResponse("Updated Successfully!!", safe=False)
    else:
        return JsonResponse(" This method allows only GET,PUT methods", safe=False)
