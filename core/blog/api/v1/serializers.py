from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CaregorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    # contact = serializers.ReadOnlyField() """ yani to ghesmat post ya update nshon nade """
    # contact = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = (
        serializers.SerializerMethodField()
    )  # tosh nishe methond_name="get_abs_url" ke esm tab mishe
    # category = serializers.SlugRelatedField(many = False,slug_field ='name' , queryset = Category.objects.all())
    # category = CaregorySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "contact",
            "snippet",
            "status",
            "category",
            "relative_url",
            "absolute_url",
            "published_date",
        ]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("contact", None)

        rep["category"] = CaregorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
