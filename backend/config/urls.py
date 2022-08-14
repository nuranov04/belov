from email.mime import base
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet
from videos.views import VideoViewSet
from files.views import FileViewSet
from home.views import HomeView

schema_view = get_swagger_view(title="Artur's API")

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='posts')
router.register(prefix='videos', viewset=VideoViewSet, basename='videos')
router.register(prefix='files', viewset=FileViewSet, basename='files')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('', HomeView.as_view())

]

urlpatterns += router.urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
