# Movie Data API

The Movie Data API is a RESTful API built using Django REST Framework that allows users to manage and retrieve information about movies, actors, genres, and technicians. It provides endpoints for creating, retrieving, updating, and deleting movie data, as well as associated data for actors, genres, and technicians.

## Features

- **Movie Management**: Create, retrieve, update, and delete movie data.
- **Actor Management**: Associate multiple actors with a movie.
- **Genre Management**: Associate multiple genres with a movie.
- **Technician Management**: Associate multiple technicians with a movie.
- **Pagination**: Responses are paginated for better performance and easier navigation.
- **Filtering**: Filter movies based on various fields, including related fields like actor names, genre names, and technician names.
- **Interactive API Documentation**: The API documentation is available through Swagger and ReDoc interfaces.

## API Endpoints

### Movies

- `GET /movie/`: Retrieve a list of movies with pagination and filtering support.
- `POST /movie/`: Create a new movie, including associated actors, genres, and technicians.
- `GET /movie/{id}/`: Retrieve details of a specific movie.
- `PUT /movie/{id}/`: Update an existing movie, including associated actors, genres, and technicians.
- `PATCH /movie/{id}/`: Partially update an existing movie.
- `DELETE /movie/{id}/`: Delete an existing movie.

### Pagination

- `page_size`: The number of items to include in each page of results. Default is 3.
- `page_size_query_param`: The query parameter used to override the page size. Default is `page_size`.
- `max_page_size`: The maximum number of items allowed in a single page. Default is 100.

### Filtering

The API supports filtering movies based on the following fields:

- `name`
- `year`
- `rating`
- `actors__name`
- `genres__name`
- `technicians__name`

## Documentation

The API documentation is available through Swagger and ReDoc interfaces:

- `GET /swagger/`: Access the Swagger UI for the API documentation.
- `GET /redoc/`: Access the ReDoc UI for the API documentation.

## Installation and Setup

1. Clone the repository: `git clone https://github.com/Suryakiran09/Movie-listing-API.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create database migrations: `python manage.py makemigrations`
4. Apply database migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the API at `http://127.0.0.1:8000/`