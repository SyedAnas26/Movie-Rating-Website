from django.conf.urls import url
from DjangoBackEnd import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^movielist/$', views.getMovies),
    url(r'^upvote/$', views.RatingsApi),
    url(r'^downvote/$', views.RatingsApi),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
