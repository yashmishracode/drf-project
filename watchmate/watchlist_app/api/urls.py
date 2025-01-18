from django.urls import path , include
# from watchlist_app.api.views import movie_list , movie_detail
from watchlist_app.api.views import MovieListAV , MovieDetailAV
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='MovieListAV'),
    path('<int:pk>/' , MovieDetailAV.as_view(),name='MovieDetailAV'),
]