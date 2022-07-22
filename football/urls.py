"""football URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_nested import routers
from django.contrib import admin


from players.views import PlayerViewSet
from teams.views import TeamViewSet
from transfers.views import TransferViewSet
from tournaments.views import TournamentViewSet
from matches.views import MatchViewSet
from matches.views import EventViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'tournaments', TournamentViewSet, basename='tournaments')

# partidas
matches_router = routers.NestedSimpleRouter(
    router, r'tournaments', lookup='tournament')
matches_router.register(r'matches', MatchViewSet, basename='matches')

events_router = routers.NestedSimpleRouter(
    matches_router, r'matches', lookup='match')
events_router.register(r'events', EventViewSet, basename='events')

schema_view = get_schema_view(
    openapi.Info(
        title="Football API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(matches_router.urls)),
    path(r'', include(events_router.urls)),

    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),


    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
]
