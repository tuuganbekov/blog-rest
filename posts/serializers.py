from rest_framework import serializers

from .models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body",]
        # exclude = ["body",]


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    created_at = serializers.DateTimeField("%d-%m-%Y")

    def create(self, validated_data):
        print("validated data:", validated_data)
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        instance.body = validated_data.get("body")
        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(type(representation["created_at"]))
        # representation["title"] = f"Title: {representation['title'].upper()}"
        # representation["new_field"] = "this is new field"
        return representation
