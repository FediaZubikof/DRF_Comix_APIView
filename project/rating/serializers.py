from rest_framework import serializers
from .models import Rating, Comic


class ComicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200, label='Название комикса')
    author = serializers.CharField(max_length=100, label='Автор комикса')
    rating_id = serializers.IntegerField(label='Рейтинг комикса')

    class Meta:
        model = Comic
        fields = (
            'id',
            'title',
            'author',
            'rating_id',
        )

    def create(self, validated_data):
        return Comic.objects.create(**validated_data)
    # def create(self, validated_data):
    #     return Comic.objects.create(
    #         id=validated_data.get('id'),
    #         title=validated_data.get('title'),
    #         author=validated_data.get('author'),
    #         rating=validated_data.get('rating'),
    #     )

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.rating_id = validated_data.get('rating_id', instance.rating_id)
        instance.save()
        return instance


class RatingSerializer(serializers.ModelSerializer):
    comic_id = serializers.IntegerField(label='Ссылка на комикс')
    user_id = serializers.IntegerField(label='Идентификатор пользователя оценившего комикс')
    value = serializers.IntegerField(label='Оценка пользователя от 1 до 5')

    class Meta:
        model = Rating
        fields = (
            'comic_id',
            'user_id',
            'value',
        )

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.comic_id = validated_data.get('comic_id', instance.comic_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.value = validated_data.get('value', instance.value)

        instance.save()
        return instance

# class RatingCreateSerializer:
# def create(self, validate_data):
#     return Rating.objects.create(
#         user_id=validate_data.get('user_id'),
#         comic_id=validate_data.get('comic_id'),
#         value=validate_data.get('value'),
#     )


# class ComicCreateSerializer:
# def create(self, validate_data):
#     return Comic.objects.create(
#         user_id=validate_data.get('user_id'),
#         comic_id=validate_data.get('comic_id'),
#         value=validate_data.get('value'),
#         rating=validate_data.get('rating'),
#     )
