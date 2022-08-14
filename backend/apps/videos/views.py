from rest_framework.viewsets import ReadOnlyModelViewSet

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoViewSet(ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
