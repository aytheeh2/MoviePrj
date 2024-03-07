# Movie Management System Readme

This Movie Management System is a Django-based web application designed to facilitate the management of movies. It provides functionalities to view, add, edit, and delete movies in a user-friendly interface.

## Features

- **View Movies**: Browse through a list of available movies.
- **Movie Details**: View detailed information about each movie.
- **Add Movie**: Add a new movie to the database.
- **Edit Movie**: Modify existing movie details.
- **Delete Movie**: Remove a movie from the database.

## URL Endpoints

- **Home**: [http://localhost:8000/](http://localhost:8000/) (List of movies)
- **Movie Details**: [http://localhost:8000/details/<int:pk>/](http://localhost:8000/details/<int:pk>/) (Details of a specific movie)
- **Add Movie**: [http://localhost:8000/addmovie/](http://localhost:8000/addmovie/) (Add a new movie)
- **Edit Movie**: [http://localhost:8000/edit_movie/<int:pk>/](http://localhost:8000/edit_movie/<int:pk>/) (Edit details of a specific movie)
- **Delete Movie**: [http://localhost:8000/delete_movie/<int:pk>/](http://localhost:8000/delete_movie/<int:pk>/) (Delete a specific movie)
