from django.urls import path
from .import views
app_name = 'movie'
urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
    path('details<int:pk>', views.MovieDetails.as_view(), name='details'),
    path('addmovie', views.MovieAdd.as_view(), name='add_movie'),
    # path('addmovie1', views.add_movie1, name='add_movie1'),
    path('edit_movie<int:pk>', views.MovieEdit.as_view(), name='edit_movie'),
    path('delete_movie<int:pk>', views.MovieDelete.as_view(), name='delete_movie'),
]
