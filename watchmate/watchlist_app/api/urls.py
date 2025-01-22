from django.urls import path
from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamingPlatformAV, StreamingPlatformdetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),  
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),  
    path('stream/', StreamingPlatformAV.as_view(), name="stream"),  
    path('stream/<int:pk>/', StreamingPlatformdetailAV.as_view(), name='streamingplatform-detail'),
]