from rest_framework import serializers
from dailybey.models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    date = serializers.DateField(required=False)
    time = serializers.TimeField(required=False)
    body = serializers.CharField(max_length=5000)
   # image = serializers.ImageField(allow_empty_file=True)
    url = serializers.URLField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new Article instance, given the validated data.
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Article instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        #instance.image = validated_data.get('image', instance.image)
        instance.body = validated_data.get('body', instance.body)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance