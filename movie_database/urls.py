from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from movie_database import settings

API_PREFIX = 'api'

urlpatterns = [
    path(f'{API_PREFIX}/v1/', include('movies.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path(f'{API_PREFIX}/schema/', SpectacularAPIView.as_view(), name='schema'),
        path(f'{API_PREFIX}/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        # path(f'{API_PREFIX}/redocs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]