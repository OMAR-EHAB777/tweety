from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tweets.api import views as qv

router = DefaultRouter()
router.register(r"tweets", qv.TweetsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("tweets/<slug:slug>/comments/",
         qv.commentsListAPIView.as_view(),
         name="comments-list"),

    path("tweets/<slug:slug>/comments/",
         qv.commentsCreateAPIView.as_view(),
         name="comments-create"),
    path("comments/<int:pk>/",
         qv.commentRUDAPIView.as_view(),
         name="comment-detail"),

    path("comments/<int:pk>/like/",
         qv.commentLikeAPIView.as_view(),
         name="comment-like")
]