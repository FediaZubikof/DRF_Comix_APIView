from .models import Comic, Rating
from .serializers import ComicSerializer, RatingSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django.db.models import Count, Avg


# Create your views here.
class RatingPostViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = RatingSerializer

    def post(self, request):
        ratings = request.data
        # Create a ratings from the above data
        serializer = self.serializer_class(data=ratings)
        if serializer.is_valid(raise_exception=True):
            ratings_saved = serializer.save()
        return Response({"success": "Rating '{}' created successfully".format(ratings_saved.value)})


class ComicPostViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = ComicSerializer

    def post(self, request):
        comics = request.data
        serializer = self.serializer_class(data=comics)
        if serializer.is_valid(raise_exception=True):
            comics_saved = serializer.save()
        return Response({"success": "Comic '{}' created successfully".format(comics_saved.title)})


class RatingGetViewSet(APIView):
    serializer_class = RatingSerializer
    permission_classes = [AllowAny]

    def get(self, request):  # Способ извлечение из БД
        rating = Rating.objects.all()
        # the many param informs the serializer that it will be serializing more than a single rating.
        serializer = self.serializer_class(rating, many=True)
        result = Rating.objects.filter(comic_id='1').aggregate(
            Avg('value')
        )
        print(result)
        # return Response({"rating": serializer.data})
        return Response({"rating": result})


class ComicGetViewSet(APIView):
    serializer_class = ComicSerializer
    permission_classes = [AllowAny]

    def get(self, request):  # Способ извлечение из БД
        comic = Comic.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = self.serializer_class(comic, many=True)

        return Response({"comic": serializer.data})


class RatingPutViewSet(APIView):
    permission_classes = [AllowAny]
    serializer_class = RatingSerializer

    def put(self, request, pk):
        saved_rating = get_object_or_404(Rating.objects.all(), pk=pk)
        data = request.data
        serializer = self.serializer_class(instance=saved_rating, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            rating_saved = serializer.save()
        return Response({
            "success": "Rating '{}' updated successfully".format(rating_saved.value)
        })

    def delete(self, request, pk):
        # Get object with this pk
        rating = get_object_or_404(Rating.objects.all(), pk=pk)
        rating.delete()
        return Response({
            "message": "Rating with id `{}` has been deleted.".format(pk)
        }, status=204)


class ComicPutViewSet(APIView):
    serializer_class = ComicSerializer
    permission_classes = [AllowAny]

    def put(self, request, pk):
        saved_comic = get_object_or_404(Comic.objects.all(), pk=pk)
        data = request.data
        serializer = self.serializer_class(instance=saved_comic, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comic_saved = serializer.save()
        return Response({
            "success": "Comic '{}' updated successfully".format(comic_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        comic = get_object_or_404(Comic.objects.all(), pk=pk)
        comic.delete()
        return Response({
            "message": "Comic with id `{}` has been deleted.".format(pk)
        }, status=204)
