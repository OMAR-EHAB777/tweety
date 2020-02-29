from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tweets.api.permissions import IsAuthorOrReadOnly
from tweets.api.serializers import commentsSerializer, tweetsSerializer
from tweets.models import tweets, comments

class TweetsViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for tweets."""
    queryset = tweets.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = tweetsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class commentsCreateAPIView(generics.CreateAPIView):
    """Allow users to comment a tweet instance if they haven't already."""
    queryset = comments.objects.all()
    serializer_class = commentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        tweets = get_object_or_404(tweets, slug=kwarg_slug)

        if tweets.comments.filter(author=request_user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(author=request_user, tweets=tweets)


class commentsListAPIView(generics.ListAPIView):
    """Provide the comments queryset of a specific tweets instance."""
    serializer_class = commentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return comments.objects.filter(tweets__slug=kwarg_slug).order_by("-created_at")


class commentLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an comment instance."""
    serializer_class = commentsSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an comments instance."""
        comments = get_object_or_404(comments, pk=pk)
        user = request.user

        comments.voters.remove(user)
        comments.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comments, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an comments instance."""
        comments = get_object_or_404(comments, pk=pk)
        user = request.user

        comments.voters.add(user)
        comments.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comments, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

class commentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for and comment instance to it's author."""
    queryset = comments.objects.all()
    serializer_class = commentsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]