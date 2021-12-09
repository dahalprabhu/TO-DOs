from rest_framework import fields, serializers
from . models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=50)
    # email = serializers.EmailField(max_length=50)
    # date = serializers.DateTimeField(initial=datetime.datetime.now)

    # def create(self, validated_data):
    #     return Post.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.save()
    #     return instance
