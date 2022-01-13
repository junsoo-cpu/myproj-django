from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from animation.models import Profile
from animation.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


profile_list = ListAPIView.as_view(
    queryset=Profile.objects.all(),
    serializer_class=ProfileSerializer,
)