# Author: Justin Huang
# GitHub username: huangjus
# Date: 3/15/23
# Description: defines three classes: Movie, StreamingService, and StreamingGuide.
# The Movie class is used to represent a movie with its title, genre, director, and year of release.
# The StreamingService class is used to represent a streaming service with its name and catalog of movies.
# The StreamingGuide class is used to represent a streaming guide with a list of streaming services, and
# provides a method to search for a movie across all services.

class Movie:
    """A class representing a movie."""

    def __init__(self, title, genre, director, year):
        """Initialize the Movie object with title, genre, director, and year."""
        self.__title = title
        self.__genre = genre
        self.__director = director
        self.__year = year

    def get_title(self):
        """Return the title of the movie."""
        return self.__title

    def get_genre(self):
        """Return the genre of the movie."""
        return self.__genre

    def get_director(self):
        """Return the director of the movie."""
        return self.__director

    def get_year(self):
        """Return the year the movie was released."""
        return self.__year


class StreamingService:
    """A class representing a streaming service."""

    def __init__(self, name):
        """Initialize the StreamingService object with a name and an empty catalog."""
        self.__name = name
        self.__catalog = {}

    def get_name(self):
        """Return the name of the streaming service."""
        return self.__name

    def get_catalog(self):
        """Return the catalog of movies."""
        return self.__catalog

    def add_movie(self, movie):
        """Add a movie to the catalog."""
        self.__catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """Remove a movie from the catalog by its title."""
        if title in self.__catalog:
            del self.__catalog[title]


class StreamingGuide:
    """A class representing a streaming guide."""

    def __init__(self):
        """Initialize the StreamingGuide object with an empty list of streaming services."""
        self.__streaming_services = []

    def add_streaming_service(self, streaming_service):
        """Add a streaming service to the list."""
        self.__streaming_services.append(streaming_service)

    def delete_streaming_service(self, name):
        """Remove a streaming service from the list by its name."""
        self.__streaming_services = [service for service in self.__streaming_services if service.get_name() != name]

    def who_streams_this_movie(self, title):
        """
        Return a dictionary with the movie's title, year, and the list of streaming services that have it available.
        If the movie is not available on any service, return None.
        """
        movie_info = None
        for service in self.__streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                movie = catalog[title]
                if movie_info is None:
                    movie_info = {'title': title, 'year': movie.get_year(), 'services': []}
                movie_info['services'].append(service.get_name())
        return movie_info
