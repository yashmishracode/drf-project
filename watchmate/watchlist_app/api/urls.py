from django.urls import path , include
# from watchlist_app.api.views import movie_list , movie_detail
from watchlist_app.api.views import WatchListAV , WatchDetailAV,StreamingPlatformAV
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='MovieListAV'),
    path('<int:pk>/' , WatchDetailAV.as_view(),name='MovieDetailAV'),
    path('stream/',StreamingPlatformAV.as_view(),name='StreamingPlatformAV')
]