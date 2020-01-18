from rest_framework import serializers
from tweets.models import tweets, comments


class commentsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    tweets_slug = serializers.SerializerMethodField()

    class Meta:
        model = comments
        exclude = ["tweets", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_tweets_slug(self, instance):
        return instance.tweets.slug


class tweetsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    user_has_commented = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = tweets
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()