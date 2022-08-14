from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import File
from .serializers import FileSerializer
from core.permissions import IsSubscriber

class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSubscriber]
