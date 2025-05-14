from django.urls import path

from movies.views.views import MovieDetailsView, MovieListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
]