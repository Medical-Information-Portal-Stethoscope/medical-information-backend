from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import UserSerializer
from likes import services
from likes.models import LikeDislike


class LikedMixin:
    @action(methods=['POST'], detail=True, url_path='vote/(?P<vote_type>\\w+)', permission_classes=(IsAuthenticated,),)
    def vote(self, request, pk=None, vote_type=None):
        """Likes or dislikes obj depending on the type of voice (like or dislike).
        """
        votes = {'like': LikeDislike.LIKE, 'dislike': LikeDislike.DISLIKE}
        obj = self.get_object()
        if vote_type not in votes:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        services.add_likedislike(obj, request.user, votes[vote_type])
        return Response()

    @action(methods=['POST'], detail=True, permission_classes=(IsAuthenticated,),)
    def unvote(self, request, pk=None):
        """Removes the user's voice from obj.
        """
        obj = self.get_object()
        services.remove_vote(obj, request.user)
        return Response()

    @action(methods=['GET'], detail=True, url_path='votes/(?P<votes_group>\\w+)')
    def votes(self, request, pk=None, votes_group=None):
        """Get fans or haters obj.
        """
        votes = {'fans': LikeDislike.LIKE, 'haters': LikeDislike.DISLIKE}
        obj = self.get_object()
        if votes_group not in votes:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        users = services.get_group(obj, votes[votes_group])
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
