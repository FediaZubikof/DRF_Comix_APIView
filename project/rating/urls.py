from django.urls import path
from .views import (
    RatingPostViewSet,
    ComicPostViewSet,
    RatingGetViewSet,
    ComicGetViewSet,
    RatingPutViewSet,
    ComicPutViewSet,
)

app_name = 'rating'

urlpatterns = [
    path('rating/', RatingPostViewSet.as_view(), name='rating'),
    path('comic/', ComicPostViewSet.as_view(), name='comic'),
    path('get_rating/', RatingGetViewSet.as_view(), name='get-rating'),
    path('get_comic/', ComicGetViewSet.as_view(), name='get-comic'),
    path('put_rating/<int:pk>', RatingPutViewSet.as_view(), name='put-rating'),
    path('put_comic/<int:pk>', ComicPutViewSet .as_view(), name='put-comic'),
]
